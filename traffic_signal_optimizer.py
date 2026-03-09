import pandas as pd

# Load dataset
data = pd.read_csv("region_traffic.csv")

# Calculate average traffic
avg_traffic = data["all_motor_vehicles"].mean()

# Function to recommend signal timing
def recommend_signal_time(vehicle_count):

    if vehicle_count > avg_traffic * 1.5:
        return 120   # heavy traffic
    elif vehicle_count > avg_traffic:
        return 90    # moderate traffic
    else:
        return 60    # light traffic


# Apply recommendation
data["recommended_signal_time"] = data["all_motor_vehicles"].apply(recommend_signal_time)

# Show results
results = data[["region_name", "all_motor_vehicles", "recommended_signal_time"]]

print(results.head(20))
