import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("region_traffic.csv")

# Define congestion threshold
threshold = data["all_motor_vehicles"].mean()

# Create congestion column
data["congestion"] = data["all_motor_vehicles"].apply(
    lambda x: 1 if x > threshold else 0
)

print("Congestion threshold:", threshold)

# Show sample
print(data[["region_name", "all_motor_vehicles", "congestion"]].head())

# Plot congestion distribution
congestion_counts = data["congestion"].value_counts()

congestion_counts.plot(kind="bar")

plt.title("Traffic Congestion Distribution")
plt.xlabel("Congestion (1 = High, 0 = Low)")
plt.ylabel("Number of Records")

plt.show()
