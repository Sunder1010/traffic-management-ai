# Traffic Management AI

This project analyzes regional traffic data and uses data science techniques to understand traffic patterns.

## Dataset
The dataset contains vehicle traffic counts categorized by:
- Region
- Road category
- Vehicle types
- Year

## Features
- Traffic data analysis
- Identify regions with highest traffic
- Visualization of traffic patterns
- Foundation for traffic prediction AI

## Technologies Used
- Python
- Pandas
- Matplotlib
- Scikit-learn

## Project Structure

traffic-management-ai  
│  
├── region_traffic.csv  
├── traffic_analysis.py  
├── requirements.txt  
└── README.md  

## Future Improvements
- Traffic congestion prediction using machine learning
- Traffic trend forecasting
- Smart traffic signal optimization

  ## Machine Learning Model

The project includes a Random Forest model that predicts total traffic volume based on vehicle categories.

The model uses:
- pedal cycles
- two wheeled vehicles
- cars and taxis
- buses
- light goods vehicles
- heavy goods vehicles

## Traffic Congestion Detection

This module detects traffic congestion levels using traffic volume data.

Congestion is determined by comparing vehicle counts against the dataset average.

Outputs:
- Congestion classification (High / Low)
- Visualization of congestion distribution

## Interactive Dashboard

This project includes a Streamlit dashboard for exploring traffic data.

Run the dashboard:

streamlit run traffic_dashboard.py
