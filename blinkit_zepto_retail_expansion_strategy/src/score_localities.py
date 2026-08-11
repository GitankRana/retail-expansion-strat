import pandas as pd

df = pd.read_csv("data/delhi_locality_expansion_data.csv")

# Weighted decision framework:
# Demand 32%, Online Grocery 20%, Accessibility 18%, Income 16%, Competition gap 14%.
df["Expansion_Score"] = (
    0.32*df["Demand_Index"] +
    0.20*df["Online_Grocery_Index"] +
    0.18*df["Delivery_Accessibility_Index"] +
    0.16*df["Income_Index"] +
    0.14*(100-df["Competition_Index"])
).round(1)

df["Priority_Tier"] = pd.cut(
    df["Expansion_Score"],
    bins=[-1,62,70,78,101],
    labels=["Low Priority","Watchlist","Priority 2","Priority 1"]
)

print("\nTop 15 expansion zones:\n")
print(df.sort_values("Expansion_Score",ascending=False)[[
    "Locality","Zone","Demand_Index","Competition_Index",
    "Delivery_Accessibility_Index","Expansion_Score","Priority_Tier"
]].head(15).to_string(index=False))

print("\nZone summary:\n")
print(df.groupby("Zone").agg(
    Localities=("Locality","count"),
    Avg_Demand=("Demand_Index","mean"),
    Avg_Competition=("Competition_Index","mean"),
    Avg_Accessibility=("Delivery_Accessibility_Index","mean"),
    Avg_Expansion_Score=("Expansion_Score","mean"),
).round(1).sort_values("Avg_Expansion_Score",ascending=False))
