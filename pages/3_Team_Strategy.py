import streamlit as st
import pandas as pd
import altair as alt

# Load matches dataset
matches = pd.read_csv("data/matches.csv")

# Page Config
st.set_page_config(page_title="Team Strategy Insights", layout="wide")

# CSS Styling
st.markdown("""
    <style>
        .page-title {
            font-size: 42px;
            font-weight: bold;
            text-align: center;
            color: white;
            margin-bottom: 20px;
        }
        .highlight-box {
            background: #fefefe;
            border: 2px solid #FF4B4B;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            font-size: 20px;
            font-weight: 600;
            color: #333;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-top: 10px;
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
        .kpi-card {
            background-color: #f9f9f9;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-top: 20px;
        }
        .metric-title {
            font-size: 22px;
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
        }
        .team-strip {
            background-color: #fafafa;
            padding: 20px;
            border-radius: 10px;
            font-size: 18px;
            display: flex;
            justify-content: space-around;
            align-items: center;
        }
        .team {
            text-align: center;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='page-title'>📋 Team Strategy Insights</div>", unsafe_allow_html=True)

# Team Selection
teams = matches['team1'].dropna().unique()
selected_team = st.selectbox("Select a Team", sorted(teams))

# Filter matches for selected team
team_matches = matches[(matches['team1'] == selected_team) | (matches['team2'] == selected_team)]

# Toss win vs match win conversion
team_matches['toss_and_win'] = team_matches.apply(
    lambda row: row['toss_winner'] == row['winner'] and row['toss_winner'] == selected_team, axis=1
)
toss_effectiveness = team_matches['toss_and_win'].mean() * 100

# KPI Display: Toss-to-Win Conversion Rate
kpi1 = st.columns(1)[0]  # single column for now
with kpi1:
    st.markdown(f"<div class='highlight-box'>🎲<br><div class='metric-title'>Toss-to-Win Conversion Rate</div><h3 style='color: black;'>{toss_effectiveness:.2f}%</h3></div>", unsafe_allow_html=True)

# Bat first vs chase win analysis
bat_first = team_matches[(team_matches['toss_winner'] == selected_team) & 
                         (team_matches['toss_decision'] == 'bat') & 
                         (team_matches['winner'] == selected_team)]

chase = team_matches[(team_matches['toss_winner'] == selected_team) & 
                     (team_matches['toss_decision'] == 'field') & 
                     (team_matches['winner'] == selected_team)]

# Batting strategy results (Bar chart)
st.markdown("<div class='chart-box'><h4 style='color: black;'>🏆 Batting First vs Chasing (Wins)</h4></div>", unsafe_allow_html=True)

# Data Preparation
batting_strategy_data = pd.DataFrame({
    'Strategy': ['Bat First', 'Chase'],
    'Wins': [len(bat_first), len(chase)]
})

# Altair Bar Chart with more spacing and adjustable size
bar_chart = alt.Chart(batting_strategy_data).mark_bar(
    size=60  # Increase bar size for more space
).encode(
    x=alt.X('Strategy', title='Strategy', sort=None),
    y=alt.Y('Wins', title='Wins', scale=alt.Scale(domain=[0, max(batting_strategy_data['Wins']) + 2])),
    color='Strategy',
    tooltip=['Strategy', 'Wins']
).properties(
    width=600,  # Set a fixed width for the chart
    height=400  # Adjust the height of the chart for better readability
).configure_mark(
    opacity=0.8  # Slightly reduce opacity for a smoother look
)

# Display chart with dynamic size adjustment
st.altair_chart(bar_chart, use_container_width=True)
