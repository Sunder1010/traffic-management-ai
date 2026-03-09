import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("region_traffic.csv")

# Select features
features = data[[
    "pedal_cycles",
    "two_wheeled_motor_vehicles",
    "cars_and_taxis",
    "buses_and_coaches",
    "lgvs",
    "all_hgvs"
]]

# Target variable
target = data["all_motor_vehicles"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

# Train model
model = RandomForestRegressor()

model.fit(X_train, y_train)

# Evaluate model
score = model.score(X_test, y_test)

print("Model Accuracy:", score)
