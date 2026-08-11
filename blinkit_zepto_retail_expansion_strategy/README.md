# Retail Expansion Strategy — Blinkit / Zepto

**Independent market strategy project | Delhi NCR**

## Objective
Identify high-potential Delhi localities for quick-commerce expansion using a structured, data-driven market prioritization framework.


## Business question
If a quick-commerce player has limited dark-store / micro-fulfilment capacity, **which Delhi localities should be evaluated first for expansion?**

## What I built
- Modeled a dataset covering **120 Delhi localities**
- Evaluated demand, household/income attractiveness, online-grocery propensity, delivery accessibility, competition and commercial-rent pressure
- Created a weighted **Expansion Score**
- Segmented localities into Priority 1, Priority 2, Watchlist and Low Priority
- Prepared data for a Power BI dashboard covering market opportunity, competitive intensity and expansion recommendations

## Decision framework

| Factor | Weight | Why it matters |
|---|---:|---|
| Demand Index | 32% | Captures underlying order potential |
| Online Grocery Index | 20% | Indicates digital grocery adoption |
| Delivery Accessibility | 18% | Indicates operational feasibility |
| Income Index | 16% | Proxy for purchasing power |
| Competition Gap | 14% | Rewards markets with lower competitive intensity |

**Expansion Score = 0.32×Demand + 0.20×Online Grocery + 0.18×Accessibility + 0.16×Income + 0.14×(100−Competition)**

### Priority rules
- **Priority 1:** Score ≥ 78
- **Priority 2:** 70–77.9
- **Watchlist:** 62–69.9
- **Low Priority:** < 62

## Power BI dashboard

Build the dashboard with `data/delhi_locality_expansion_data.csv`.

### Page 1 — Market Overview
KPI cards:
- Total localities
- Average expansion score
- Number of Priority 1 zones
- Average demand index

Charts:
- Expansion score by locality
- Average score by Delhi zone
- Demand vs competition scatter plot

### Page 2 — Expansion Prioritization
Use:
- Map / locality table
- Conditional formatting by Priority Tier
- Top 15 locality ranking
- Slicers for Zone and Priority Tier

### Page 3 — Decision Drivers
Use a scatter plot or decomposition-style visual to show:
- Demand
- Online grocery adoption
- Accessibility
- Competition
- Income

## Key strategic interpretation
The model intentionally avoids choosing locations on demand alone. A locality can have strong demand but still be unattractive if competitive intensity is high or operational accessibility is weak.

The recommended expansion process is therefore:

**Screen → Score → Prioritize → Validate on-ground → Pilot → Scale**


## Repository structure

```text
retail-expansion-strategy/
├── data/
│   ├── delhi_locality_expansion_data.csv
│   ├── top_15_expansion_zones.csv
│   └── zone_summary.csv
├── src/
│   └── score_localities.py
├── docs/
│   └── powerbi_dashboard_spec.md
└── README.md
```

## Skills demonstrated
**Market Research · Strategy · Data Analysis · Decision Frameworks · Power BI · Excel/CSV · Competitive Analysis · Business Storytelling**
