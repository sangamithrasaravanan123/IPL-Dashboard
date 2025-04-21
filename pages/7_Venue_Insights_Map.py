import streamlit as st
import pandas as pd
import plotly.express as px

# Load matches data
matches = pd.read_csv("data/matches.csv")

# Page Config
st.set_page_config(page_title="🌍 Venue Insights Across Cities", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
        .page-title {
            font-size: 42px;
            font-weight: bold;
            text-align: center;
            color: white;
            margin-bottom: 0;
        }
        .kpi-card {
            background-color: #f9f9f9;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        .metric-title {
            font-size: 22px;
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
        }
        .chart-box {
            background-color: #fff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(0,0,0,0.04);
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='page-title'>🌍 Venue Insights Across Cities</div>", unsafe_allow_html=True)

# Filter data by venue and remove NaN values in 'result_margin'
venue_data = matches[matches['city'].notna()]
venue_data = venue_data[venue_data['result_margin'].notna()]

# KPI Cards for Venue Insights
total_matches = venue_data.shape[0]
avg_result_margin = venue_data['result_margin'].mean()

kpi1, kpi2 = st.columns(2)
with kpi1:
    st.markdown(f"<div class='kpi-card'>📊<br><div class='metric-title'>Total Matches Played</div><h3 style='color: black;'>{total_matches}</h3></div>", unsafe_allow_html=True)

with kpi2:
    st.markdown(f"<div class='kpi-card'>📏<br><div class='metric-title'>Average Result Margin</div><h3 style='color: black;'>{round(avg_result_margin, 2)}</h3></div>", unsafe_allow_html=True)

# Create map visualization
fig = px.scatter_geo(venue_data, locations="city", size="result_margin", color="winner",
                     hover_name="city", hover_data=["result_margin", "season", "team1", "team2"],
                     color_continuous_scale="Viridis", title="Venue Performance Map")

# Display map
st.markdown("<div class='chart-box'>", unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)
