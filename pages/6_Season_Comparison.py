import streamlit as st
import pandas as pd

# Load matches data
matches = pd.read_csv("data/matches.csv")

# Page Config
st.set_page_config(page_title="Season-wise Team Performance", layout="wide")

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
        .section-title {
            font-size: 28px;
            font-weight: 700;
            color: gray;
            margin-top: 40px;
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
st.markdown("<div class='page-title'>📆 Season-wise Team Performance</div>", unsafe_allow_html=True)

# Select team
teams = matches['team1'].dropna().unique()
selected_team = st.selectbox("Select a Team", sorted(teams))

# Filter matches for the selected team
team_seasons = matches[matches['team1'] == selected_team]
team_seasons = pd.concat([team_seasons, matches[matches['team2'] == selected_team]])

# Calculate wins and losses by season
season_performance = team_seasons.groupby('season')['winner'].apply(
    lambda x: x.eq(selected_team).sum()  # Count wins
).reset_index(name='Wins')
season_performance['Losses'] = team_seasons.groupby('season')['id'].count() - season_performance['Wins']

# KPI Cards for Wins and Losses
kpi1, kpi2 = st.columns(2)
with kpi1:
    st.markdown(f"<div class='kpi-card'>🏆<br><div class='metric-title'>Total Wins</div><h3 style='color: black;'>{season_performance['Wins'].sum()}</h3></div>", unsafe_allow_html=True)

with kpi2:
    st.markdown(f"<div class='kpi-card'>❌<br><div class='metric-title'>Total Losses</div><h3 style='color: black;'>{season_performance['Losses'].sum()}</h3></div>", unsafe_allow_html=True)

# Season-wise Performance Bar Chart
st.subheader(f"{selected_team} - Season-wise Win/Loss")
st.markdown("<div class='chart-box'>", unsafe_allow_html=True)

# Plot performance
st.bar_chart(season_performance.set_index('season')[['Wins', 'Losses']], use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)
