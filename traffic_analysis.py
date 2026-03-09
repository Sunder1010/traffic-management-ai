import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("region_traffic.csv")

# Show dataset info
print("Dataset shape:", data.shape)
print(data.head())

# Group by region
traffic_by_region = data.groupby("region_name")["all_motor_vehicles"].sum()

# Sort values
top_regions = traffic_by_region.sort_values(ascending=False).head(10)

print("\nTop traffic regions:")
print(top_regions)

# Plot graph
top_regions.plot(kind="bar")

plt.title("Top 10 Regions by Traffic Volume")
plt.xlabel("Region")
plt.ylabel("Vehicle Count")

plt.tight_layout()
plt.show()
