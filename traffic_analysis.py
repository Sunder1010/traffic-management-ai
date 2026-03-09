import pandas as pd

# Load dataset
data = pd.read_csv("region_traffic.csv")

# Show basic information
print("Dataset shape:", data.shape)
print(data.head())

# Total vehicles per region
traffic_by_region = data.groupby("region_name")["all_motor_vehicles"].sum()

print("\nTraffic by region:")
print(traffic_by_region.sort_values(ascending=False).head(10))
