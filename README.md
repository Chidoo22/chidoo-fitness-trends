# 🏃‍♀️ Chidoo Fitness Trends

> *My personal health & fitness journey — from raw iPhone data to a fully interactive dashboard.*

I built this project for myself. No tutorials, no sample datasets, no fake numbers — just my real Apple Health data going back to **2020**, turned into something I can actually learn from and be proud of.

This is part of my data analytics portfolio, but more than that, it's a window into my personal fitness and weight loss journey. Every step, every workout, every resting heart rate reading in here is mine.

---

## 🌟 What This Dashboard Does

A single-file HTML dashboard that runs directly in your browser — no server, no login, no setup. Just open and go.

### 📊 Overview Tab
- **4 KPI cards** — Total Steps, Avg Resting Heart Rate, Total Workouts, Calories Burned
- **Composite Health Score** — a single 0–100 score calculated from all metrics combined
- **Activity Heatmap** — GitHub-style calendar showing daily step activity over the past year
- **Achievement Badges** — milestone rewards (10K day, 20K day, personal bests)
- **Streak & Level System** — gamified consistency tracking

### 🏃 Activity Tab
- **Daily Steps** bar chart with 7-day moving average overlay
- **Resting Heart Rate** trends over time
- **Active Calories** burned per day
- **Workout Types** breakdown — how many sessions of each type
- **Workout Duration** scatter plot by type across time

### ⚖️ Weight & Health Tab
- **Weight reconstruction** — modelled from activity and calorie data
- **VO2 Max** tracker with first vs latest reading comparison
- **Steps vs Weight** correlation scatter
- **Calories vs Weight** correlation scatter

### 📈 Analytics Tab
- **Feature importance** — which metrics most influence weight
- **Model accuracy** plot — predicted vs actual weight
- **Monthly activity** trends

### 🔮 Prediction Tab
- Enter your current weight, goal weight, and daily calorie intake
- Get a projected goal date with 3 calorie scenarios (1,500 / your target / 2,000 kcal)

---

## 💡 The Story Behind It

I started tracking my health seriously through the **Apple Health app on my iPhone** — steps, workouts, heart rate, everything. After a while I had years of data sitting there but no good way to actually *see* it or understand my progress.

As someone transitioning into data analytics, I decided to build my own solution. I wrote a **Python data pipeline** that converts the raw Apple Health export into clean, structured JSON, then built a **fully interactive web dashboard** around it.

No third-party fitness apps. No subscriptions. Just my data, my way.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Dashboard | HTML, CSS, JavaScript (single file) |
| Charts | [Plotly.js](https://plotly.com/javascript/) |
| Design | Glassmorphic UI — dark/light mode, CSS variables |
| Data Pipeline | Python (pandas, xml.etree) |
| Data Source | Apple Health (iPhone export) |
| Hosting | Runs locally — open the HTML file directly |

---

## 🚀 How to Use It (For Your Own Data)

### Step 1 — Export from iPhone
On your iPhone: **Health app → your profile photo → Export All Health Data**  
This creates an `export.zip` file. Send it to your computer.

### Step 2 — Run the Python script
```bash
# Install dependencies (first time only)
pip install -r tools/requirements.txt

# Convert your export to dashboard JSON
python tools/apple_health_to_json.py --zip "path/to/export.zip"
```
This generates `projects/dashboards/fitness-dashboard/fitness_data.json`.

### Step 3 — Import into the dashboard
1. Open `projects/dashboards/fitness-dashboard/fitness_dashboard.html` in your browser
2. Click **Import** (top right)
3. Drop your `fitness_data.json` file in
4. Click **View Dashboard →**

That's it. Your data, your dashboard.

---

## 📁 Project Structure

```
chidoo-fitness-trends/
│
├── projects/
│   ├── dashboards/
│   │   ├── fitness-dashboard/
│   │   │   ├── fitness_dashboard.html      ← Main dashboard
│   │   │   ├── fitness_dashboard_v2.html   ← Experimental version
│   │   │   └── How-To-Update-Your-Dashboard.html
│   │   └── weight-model/
│   │       ├── weight_model.html           ← Weight model dashboard
│   │       └── weight_model_decoded.json   ← ML model data
│   └── sql-practice/
│       └── practice.sql                    ← SQL learning exercises
│
├── tools/
│   ├── apple_health_to_json.py             ← Data pipeline script
│   └── requirements.txt
│
└── .claude/skills/                         ← Claude Code AI skills
```

---

## 🔒 Privacy Note

My personal health data (`fitness_data.json`) is intentionally excluded from this repository via `.gitignore`. The dashboard runs on **demo data by default** so you can explore all the features without needing real data first.

---

## 📌 Skills Demonstrated

This project sits at the intersection of everything I'm building towards as a data analyst:

- **Data Engineering** — building a pipeline from raw XML health exports to structured JSON
- **Data Visualisation** — 15+ interactive Plotly.js charts across 6 dashboard tabs
- **Statistical Analysis** — trend comparisons, moving averages, period-over-period analysis
- **Predictive Modelling** — weight reconstruction and goal projection modelling
- **Front-End Development** — single-file HTML/CSS/JS dashboard with no framework dependencies
- **UX Design** — dark/light mode, responsive layout, glassmorphic design system

---

## 🗺️ What's Next

- [ ] Sleep data tab (Apple Health exports sleep too)
- [ ] Goal rings — daily step/calorie target tracking
- [ ] Day-of-week activity patterns
- [ ] Export charts as images

---

## 👩‍💻 About Me

I'm **Chido Tembo** — an Informatics graduate and aspiring data analyst based in Poland, transitioning from 2+ years in business operations. I build projects like this to sharpen my skills and tell stories through data.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chido-nicole-tembo-474793353)
[![GitHub](https://img.shields.io/badge/GitHub-Chidoo22-181717?style=flat-square&logo=github)](https://github.com/Chidoo22)
[![Email](https://img.shields.io/badge/Email-chidonicole4@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:chidonicole4@gmail.com)

---

*Built with curiosity, Python, and a lot of daily steps.* 🦶
