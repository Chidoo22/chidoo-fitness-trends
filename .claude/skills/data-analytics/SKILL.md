---
name: data-analytics
description: "Use when Chido wants to build, update, or improve an interactive data dashboard — especially fitness/health dashboards using Plotly.js and JSON data. Trigger on: 'build a dashboard', 'update my dashboard', 'add a chart', 'visualize this data', 'add a new section', 'connect this data', 'analyse this data', or any mention of the fitness dashboard, weight model, or Apple Health data. Also use for general data analysis, DAX formulas, Power BI guidance, or Tableau-style charts."
---

# Data Analytics Skill

## Chido's Dashboard Stack (What She Actually Uses)

Her dashboards are **single-file HTML** powered by:
- **Plotly.js** — interactive charts (line, bar, scatter, heatmap, histogram, indicator)
- **Vanilla HTML/CSS/JS** — no framework, no build step, opens directly in any browser
- **JSON data files** — fitness_data.json, weight_model_data.json embedded or loaded from file
- **Apple Health export** — iPhone health data (steps, heart rate, calories, weight, workouts)
- **Inter font** — via Google Fonts CDN
- **Glassmorphic dark/light mode design** — CSS variables, blur effects, animated blobs

## Existing Projects (Always Check These First)

| Project | Files | Description |
|---------|-------|-------------|
| Fitness Dashboard | `projects/dashboards/fitness-dashboard/fitness_dashboard.html` | Main dashboard — steps, heart rate, calories, workouts. Uses Plotly.js + glassmorphic design |
| Fitness Dashboard v2 | `projects/dashboards/fitness-dashboard/fitness_dashboard_v2.html` | Updated version |
| Fitness Data | `projects/dashboards/fitness-dashboard/fitness_data.json` | Apple Health JSON data |
| Weight Model | `projects/dashboards/weight-model/weight_model_data.json` | Weight tracking + prediction data |
| How-To Guide | `projects/dashboards/fitness-dashboard/How-To-Update-Your-Dashboard.html` | Jabril's guide for updating the dashboard |

## Workflow — Building / Updating a Dashboard

### Adding a new chart to the fitness dashboard
1. Read `fitness_dashboard.html` to understand current structure
2. Read `fitness_data.json` to understand available data fields
3. Add the new Plotly chart in the correct tab/section
4. Match existing design system (CSS variables, card style, color palette)
5. Save to `projects/dashboards/fitness-dashboard/`

### Building a new dashboard from scratch
1. Ask: what data? what questions should it answer?
2. Use Plotly.js CDN (current version: `https://cdn.plot.ly/plotly-2.35.0.min.js`)
3. Use single-file HTML (no server needed — works on Windows by just double-clicking)
4. Follow Chido's established design system (see Design System section below)
5. Save as `projects/dashboards/[project-name].html`

### Connecting new Apple Health data
- Apple Health exports as XML inside a ZIP
- The dashboard currently loads from an embedded JSON or uploaded file
- Python script can convert Apple Health XML → dashboard-compatible JSON

## Design System (Match This in All Dashboards)

### Colors (CSS Variables)
```css
:root {
  --bg: #060610;          /* Main background */
  --bg2: #0c0c1d;         /* Secondary background */
  --card: rgba(255,255,255,0.04);  /* Card background */
  --bdr: rgba(255,255,255,0.08);   /* Border */
  --t1: #eeeef5;          /* Primary text */
  --t2: #8888a0;          /* Secondary text */
  --em: #10b981;          /* Emerald (positive) */
  --coral: #f97316;       /* Coral (warnings) */
  --violet: #8b5cf6;      /* Violet accent */
  --cyan: #06b6d4;        /* Cyan (active states) */
  --amber: #f59e0b;       /* Amber */
  --rose: #f43f5e;        /* Rose (negative) */
  --blue: #3b82f6;        /* Blue */
}
```

### Plotly Chart Config (Use for All Charts)
```javascript
const layout = {
  paper_bgcolor: 'rgba(0,0,0,0)',
  plot_bgcolor: 'rgba(0,0,0,0)',
  font: { family: 'Inter, system-ui', color: '#8888a0', size: 11 },
  margin: { t: 30, r: 16, b: 40, l: 50 },
  xaxis: { gridcolor: 'rgba(255,255,255,0.05)', zeroline: false },
  yaxis: { gridcolor: 'rgba(255,255,255,0.05)', zeroline: false }
};
const config = { responsive: true, displayModeBar: false };
Plotly.newPlot('chart-id', traces, layout, config);
```

### Card Structure
```html
<div class="card">
  <div class="kpi-bar"></div>  <!-- colored top border -->
  <div class="card-label">Metric Name</div>
  <div class="card-value">1,234</div>
  <div class="card-sub">subtitle text</div>
</div>
```

## Power BI (Professional Work)

For Power BI report building → see `pbi-report-builder.md` in this same folder.

### DAX Formula Help (Quick Reference)
```dax
-- Total Sales
Total Sales = SUM(Sales[Amount])

-- Year-over-Year Growth
YoY Growth = DIVIDE([Current Year], [Prior Year]) - 1

-- Rolling 30-day average
30D Avg = AVERAGEX(DATESINPERIOD(Dates[Date], LASTDATE(Dates[Date]), -30, DAY), [Measure])

-- Running Total
Running Total = CALCULATE([Measure], FILTER(ALL(Dates), Dates[Date] <= MAX(Dates[Date])))
```

## Tableau-Style Charts (HTML/JS alternative)

When Tableau is not available, build equivalent charts in Plotly:
- Bar chart comparison → `Plotly.bar` with grouped/stacked mode
- Line trend → `Plotly.scatter` with `mode: 'lines'`
- KPI indicators → `Plotly.indicator` with delta
- Heatmap calendar → `Plotly.heatmap`
- Scatter with color → `Plotly.scatter` with marker.color array

## Data Analysis (Python)

For data processing before building dashboards:
```python
import pandas as pd
import json

# Load Apple Health data
df = pd.read_csv('data.csv')

# Basic analysis
df.describe()
df['date'] = pd.to_datetime(df['date'])
df.groupby(df['date'].dt.month)['steps'].mean()

# Export for dashboard
df.to_json('dashboard_data.json', orient='records', date_format='iso')
```

## Output Rules
- All dashboard HTML files → `projects/dashboards/[project-name]/`
- All data files (JSON, CSV) → same folder as the dashboard
- All SQL scripts → `projects/sql-practice/`
- Python data scripts → `tools/`
