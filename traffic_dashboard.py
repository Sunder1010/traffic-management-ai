import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Traffic Management AI Dashboard")

# Load dataset
data = pd.read_csv("region_traffic.csv")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(data.head())

# Traffic by region
traffic_by_region = data.groupby("region_name")["all_motor_vehicles"].sum()

# Show top regions
st.subheader("Top 10 Regions by Traffic Volume")
top_regions = traffic_by_region.sort_values(ascending=False).head(10)
st.write(top_regions)

# Plot graph
fig, ax = plt.subplots()
top_regions.plot(kind="bar", ax=ax)

ax.set_title("Top 10 Regions by Traffic Volume")
ax.set_xlabel("Region")
ax.set_ylabel("Vehicle Count")

st.pyplot(fig)
