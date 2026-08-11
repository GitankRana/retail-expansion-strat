# Power BI Dashboard Specification

## Recommended layout

### Page 1 — Delhi Quick-Commerce Market
**Cards:** Total Localities | Priority 1 Zones | Avg Demand | Avg Expansion Score

**Visuals**
1. Bar chart: Top 15 localities by Expansion Score
2. Column chart: Average Expansion Score by Zone
3. Scatter: Demand Index vs Competition Index
   - X = Competition Index
   - Y = Demand Index
   - Size = Estimated Households
   - Legend = Priority Tier
4. Slicers: Zone, Priority Tier

### Page 2 — Expansion Prioritization
Use a table with:
Locality | Zone | Demand | Competition | Accessibility | Expansion Score | Priority Tier

Apply conditional formatting to Expansion Score and Priority Tier.

### Page 3 — Driver Analysis
Suggested visuals:
- Demand vs Online Grocery Index
- Accessibility vs Expansion Score
- Competition vs Expansion Score
- Average driver scores by Zone

## Suggested DAX measures

```DAX
Avg Expansion Score = AVERAGE('delhi_locality_expansion_data'[Expansion_Score])

Priority 1 Count =
CALCULATE(
    COUNTROWS('delhi_locality_expansion_data'),
    'delhi_locality_expansion_data'[Priority_Tier] = "Priority 1"
)

Avg Demand = AVERAGE('delhi_locality_expansion_data'[Demand_Index])

Avg Competition = AVERAGE('delhi_locality_expansion_data'[Competition_Index])
```

## Executive takeaway format
End the dashboard with three statements:
1. **Where to expand first?**
2. **Why those markets?**
3. **What must be validated before opening capacity?**
