import pandas as pd

# Load original dataset
df_og = pd.read_csv("../Code/original_global_bleaching_environmental.csv")

# Keep only relevant columns
columns_needed = [
    "Ecoregion_Name",
    "Turbidity",
    "Depth_m",
    "Windspeed",
    "SSTA_DHW",
    "Date_Year",
    "Percent_Bleaching"
]

df_og = df_og[columns_needed]

# Convert columns to numeric
df_og["Turbidity"] = pd.to_numeric(df_og["Turbidity"], errors="coerce")
df_og["Depth_m"] = pd.to_numeric(df_og["Depth_m"], errors="coerce")
df_og["Windspeed"] = pd.to_numeric(df_og["Windspeed"], errors="coerce")
df_og["SSTA_DHW"] = pd.to_numeric(df_og["SSTA_DHW"], errors="coerce")
df_og["Percent_Bleaching"] = pd.to_numeric(df_og["Percent_Bleaching"], errors="coerce")

# Remove rows with missing values
df_og = df_og.dropna(subset=[
    "Turbidity",
    "Depth_m",
    "SSTA_DHW",
    "Percent_Bleaching"
])

# Remove rows where Percent_Bleaching is 0
df_og = df_og[df_og["Percent_Bleaching"] != 0]

# Keep only ecoregions with at least 500 rows
ecoregion_counts = df_og["Ecoregion_Name"].value_counts()
valid_ecoregions = ecoregion_counts[ecoregion_counts >= 500].index
df_og = df_og[df_og["Ecoregion_Name"].isin(valid_ecoregions)]

# Save cleaned dataset
df_og.to_csv("../Code/cleaned_data.csv", index=False)
print("Cleaned dataset saved as 'cleaned_data.csv'.")