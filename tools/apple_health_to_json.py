"""
Apple Health Export → Dashboard JSON Converter
-----------------------------------------------
Converts the export.zip from iPhone Health app into
a fitness_data.json file that works directly with the dashboard.

HOW TO USE:
    1. On your iPhone: Health app → tap your photo (top right) → Export All Health Data
    2. Send the export.zip to your Windows computer
    3. Run this script:
           python tools/apple_health_to_json.py --zip "path/to/export.zip"
    4. Open the dashboard → click Import → drop the fitness_data.json file
    5. Dashboard updates instantly!

The JSON file method is recommended over direct ZIP import for files over 50MB.
"""

import argparse
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path


def parse_apple_health(zip_path: str, out_path: str):
    zip_path = Path(zip_path)
    out_path = Path(out_path)

    print(f"\nOpening: {zip_path}")

    # --- Extract XML from ZIP ---
    with zipfile.ZipFile(zip_path, "r") as z:
        xml_files = [f for f in z.namelist() if f.lower().endswith("export.xml") or f.lower().endswith(".xml")]
        if not xml_files:
            raise FileNotFoundError(
                "No export.xml found in ZIP.\n"
                "Make sure you exported from iPhone Health app (not a different ZIP)."
            )
        print(f"Found XML: {xml_files[0]}")
        print("Reading XML... (this may take a moment for large files)")
        with z.open(xml_files[0]) as f:
            xml_text = f.read().decode("utf-8", errors="replace")

    print(f"XML size: {len(xml_text)/1024/1024:.1f} MB — parsing records...")

    # --- Parse records with regex (same approach as dashboard JS) ---
    steps_by_day = defaultdict(float)
    hr_readings = []
    cal_by_day = defaultdict(float)
    vo2_readings = []
    workouts = []

    record_re = re.compile(r'<Record\s[^>]*/>', re.DOTALL)
    workout_re = re.compile(r'<Workout\s[^>]*(?:/>|>[\s\S]*?</Workout>)', re.DOTALL)

    def get_attr(s, name):
        m = re.search(name + r'="([^"]*)"', s)
        return m.group(1) if m else ""

    total = len(xml_text)
    last_pct = 0

    for m in record_re.finditer(xml_text):
        pct = int(m.start() / total * 80)
        if pct >= last_pct + 5:
            print(f"  {pct}%...", end="\r", flush=True)
            last_pct = pct

        rec = m.group(0)
        rtype = get_attr(rec, "type")
        try:
            value = float(get_attr(rec, "value"))
        except ValueError:
            continue
        start = get_attr(rec, "startDate")
        if not start:
            continue
        date_key = start[:10]

        if rtype == "HKQuantityTypeIdentifierStepCount":
            steps_by_day[date_key] += value
        elif rtype == "HKQuantityTypeIdentifierHeartRate":
            hr_readings.append((start, value))
        elif rtype == "HKQuantityTypeIdentifierActiveEnergyBurned":
            cal_by_day[date_key] += value
        elif rtype == "HKQuantityTypeIdentifierVO2Max":
            vo2_readings.append((start, value))

    print("  80%... parsing workouts")

    for m in workout_re.finditer(xml_text):
        wk = m.group(0)
        wk_type = get_attr(wk, "workoutActivityType").replace("HKWorkoutActivityType", "")
        wk_start = get_attr(wk, "startDate")
        try:
            wk_dur = float(get_attr(wk, "duration"))
        except ValueError:
            wk_dur = 0.0
        if wk_type and wk_start:
            workouts.append((wk_type, wk_dur, wk_start))

    print("  100% — building Plotly traces...")

    # --- Build traces (exact format the dashboard expects) ---

    # FD[0]: Steps bar
    step_dates = sorted(steps_by_day.keys())
    step_vals = [round(steps_by_day[d]) for d in step_dates]
    steps_trace = {
        "marker": {"color": "#1D9E75"},
        "name": "Steps",
        "opacity": 0.5,
        "showlegend": False,
        "x": [d + "T00:00:00" for d in step_dates],
        "y": step_vals,
        "type": "bar"
    }

    # FD[1]: Steps 7-day moving average
    avg_x, avg_y = [], []
    for i in range(6, len(step_vals)):
        avg_x.append(step_dates[i] + "T00:00:00")
        avg_y.append(round(sum(step_vals[i-6:i+1]) / 7))
    steps_avg_trace = {
        "line": {"color": "#10b981", "shape": "spline", "width": 2},
        "mode": "lines",
        "name": "7d avg",
        "showlegend": False,
        "x": avg_x,
        "y": avg_y
    }

    # FD[2]: Heart rate monthly averages
    hr_by_month = defaultdict(list)
    for dt, val in hr_readings:
        hr_by_month[dt[:7]].append(val)
    hr_months = sorted(hr_by_month.keys())
    hr_trace = {
        "line": {"color": "#FF6347", "width": 2},
        "mode": "lines+markers",
        "name": "Resting HR",
        "showlegend": False,
        "x": [m + "-15T00:00:00" for m in hr_months],
        "y": [round(sum(hr_by_month[m]) / len(hr_by_month[m])) for m in hr_months]
    }

    # FD[3]: Active calories daily
    cal_dates = sorted(cal_by_day.keys())
    cal_trace = {
        "line": {"color": "#8b5cf6", "width": 2},
        "mode": "lines",
        "name": "Active Calories",
        "showlegend": False,
        "x": [d + "T00:00:00" for d in cal_dates],
        "y": [round(cal_by_day[d]) for d in cal_dates]
    }

    # FD[4]: VO2 Max
    vo2_readings.sort(key=lambda r: r[0])
    if vo2_readings:
        vo2_trace = {
            "mode": "lines+markers",
            "name": "VO2 Max",
            "showlegend": False,
            "x": [r[0][:10] + "T00:00:00" for r in vo2_readings],
            "y": [r[1] for r in vo2_readings]
        }
    else:
        vo2_trace = {
            "mode": "lines+markers",
            "name": "VO2 Max",
            "showlegend": False,
            "x": ["2020-01-01T00:00:00"],
            "y": [0]
        }

    # FD[5]: Workout types bar
    wk_type_count = defaultdict(int)
    wk_by_type = defaultdict(lambda: {"x": [], "y": []})
    for wk_type, wk_dur, wk_start in workouts:
        wk_type_count[wk_type] += 1
        wk_by_type[wk_type]["x"].append(wk_start[:10] + "T00:00:00")
        wk_by_type[wk_type]["y"].append(round(wk_dur * 10) / 10)

    wk_pairs = sorted(wk_type_count.items(), key=lambda kv: kv[1], reverse=True)
    workout_bar_trace = {
        "name": "Workout Types",
        "showlegend": False,
        "x": [p[1] for p in wk_pairs],
        "y": [p[0] for p in wk_pairs],
        "type": "bar",
        "orientation": "h"
    }

    # FD[6+]: Per-workout-type scatter traces
    workout_scatter_traces = [
        {
            "mode": "markers",
            "name": t,
            "showlegend": True,
            "x": data["x"],
            "y": data["y"]
        }
        for t, data in wk_by_type.items()
    ]

    # Assemble final traces array
    traces = [steps_trace, steps_avg_trace, hr_trace, cal_trace, vo2_trace, workout_bar_trace]
    traces.extend(workout_scatter_traces)

    # Wrap in fitness_data.json format
    output = {"traces": traces, "layout": {}}

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, separators=(",", ":"))

    size_kb = out_path.stat().st_size / 1024
    print(f"\n✅ Saved: {out_path}  ({size_kb:.0f} KB)")
    print(f"   Steps: {len(step_dates)} days")
    print(f"   Heart rate: {len(hr_readings)} readings across {len(hr_months)} months")
    print(f"   Calories: {len(cal_dates)} days")
    print(f"   VO2 Max: {len(vo2_readings)} readings")
    print(f"   Workouts: {len(workouts)} sessions, {len(wk_by_type)} types")
    print(f"\nNext step: Open the dashboard → click Import → drop fitness_data.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Apple Health export to dashboard JSON")
    parser.add_argument("--zip", default="export.zip", help="Path to Apple Health export.zip (default: export.zip)")
    parser.add_argument(
        "--out",
        default="projects/dashboards/fitness-dashboard/fitness_data.json",
        help="Output path (default: projects/dashboards/fitness-dashboard/fitness_data.json)"
    )
    args = parser.parse_args()
    parse_apple_health(args.zip, args.out)
