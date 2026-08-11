
---

# Retail Expansion Strategy — Blinkit / Zepto

**Independent Market Strategy & Data Analytics Project | Delhi NCR**

## Overview

This project simulates how a quick-commerce company such as **Blinkit** or **Zepto** could prioritize expansion into new Delhi localities using a structured, data-driven decision framework.

Instead of selecting locations based solely on demand, the model evaluates multiple business and operational factors to identify markets with the highest expansion potential.

---

## Business Problem

Quick-commerce companies operate with limited **dark stores**, delivery fleets, and capital.

**Business Question**

> If a quick-commerce company has limited expansion capacity, which Delhi localities should be prioritized for opening new dark stores?

To answer this, I developed a scoring framework that ranks localities based on market attractiveness and operational feasibility.

---

## Project Objectives

* Analyze 120 Delhi NCR localities
* Measure demand and digital grocery adoption
* Evaluate operational accessibility
* Assess purchasing power and competition
* Build an Expansion Score for each locality
* Classify markets into actionable priority tiers
* Visualize insights using Power BI

---

## Methodology

Each locality is evaluated across five key business dimensions.

| Factor                 | Weight | Purpose                             |
| ---------------------- | ------ | ----------------------------------- |
| Demand Index           | 32%    | Estimates potential order volume    |
| Online Grocery Index   | 20%    | Measures digital grocery adoption   |
| Delivery Accessibility | 18%    | Indicates operational feasibility   |
| Income Index           | 16%    | Proxy for purchasing power          |
| Competition Gap        | 14%    | Rewards lower competitive intensity |

### Expansion Score Formula

```text
Expansion Score =
0.32 × Demand Index
+ 0.20 × Online Grocery Index
+ 0.18 × Delivery Accessibility
+ 0.16 × Income Index
+ 0.14 × (100 − Competition Index)
```

---

## Priority Classification

| Tier         | Expansion Score |
| ------------ | --------------- |
| Priority 1   | ≥ 78            |
| Priority 2   | 70 – 77.9       |
| Watchlist    | 62 – 69.9       |
| Low Priority | < 62            |

---

## Power BI Dashboard

### Page 1 — Market Overview

**KPIs**

* Total Localities
* Average Expansion Score
* Priority 1 Localities
* Average Demand Index

**Visuals**

* Expansion Score by Locality
* Average Score by Delhi Zone
* Demand vs Competition Scatter Plot

---

### Page 2 — Expansion Prioritization

* Ranked Top 15 Expansion Localities
* Locality Table
* Priority Tier Heatmap
* Zone & Priority Filters
* Interactive Map

---

### Page 3 — Decision Drivers

Business drivers influencing locality rankings:

* Demand
* Online Grocery Adoption
* Accessibility
* Income
* Competition


---

## Strategic Insight

The framework intentionally avoids selecting locations based only on demand.

A locality may exhibit high demand but still be unsuitable due to:

* High competitive intensity
* Poor delivery accessibility
* Lower purchasing power
* High operational constraints

The recommended expansion workflow is:

```text
Screen
    ↓
Score
    ↓
Prioritize
    ↓
Validate On-Ground
    ↓
Pilot
    ↓
Scale
```

---

## Repository Structure

```text
retail-expansion-strategy/
│
├── data/
│   ├── delhi_locality_expansion_data.csv
│   ├── top_15_expansion_zones.csv
│   └── zone_summary.csv
│
├── src/
│   └── score_localities.py
│
├── docs/
│   └── powerbi_dashboard_spec.md
│
├── dashboard/
│   └── Retail_Expansion_Dashboard.pbix
│
├── screenshots/
│   ├── overview.png
│   ├── prioritization.png
│   └── decision_drivers.png
│
└── README.md
```

---

## Tech Stack

* Python
* Pandas
* NumPy
* Power BI
* Excel / CSV
* Git & GitHub

---

## Key Deliverables

* Market prioritization framework
* Weighted Expansion Score model
* Locality ranking engine
* Power BI executive dashboard
* Strategy-driven business recommendations

---

## Skills Demonstrated

* Market Research
* Business Strategy
* Data Analysis
* Power BI Dashboarding
* Decision Framework Design
* Competitive Analysis
* Business Storytelling
* Data Visualization
* Strategic Thinking

---

## Disclaimer

This is an **independent educational project** created to demonstrate business strategy and data analytics skills. The dataset is modeled for analytical purposes and does not represent proprietary information from Blinkit, Zepto, or any affiliated organization.
