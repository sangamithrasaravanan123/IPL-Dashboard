import streamlit as st
import pandas as pd
import altair as alt

# Load data
deliveries = pd.read_csv("data/deliveries.csv")

# Page Config
st.set_page_config(page_title="Player Insights", layout="wide")

# CSS Styling
st.markdown("""
    <style>
        .page-title {
            font-size: 42px;
            font-weight: bold;
            text-align: center;
            color: white;
            margin-bottom: 0;
        }
        .player-section {
            margin-top: 30px;
            text-align: center;
        }
        .kpi-card {
            background-color: #f9f9f9;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        .chart-box {
            background-color: #fff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(0,0,0,0.04);
            margin-top: 40px;
        }
        .metric-title {
            font-size: 22px;
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='page-title'>🧍 Player Performance Insights</div>", unsafe_allow_html=True)

# Player Selection
st.markdown("<div class='player-section'><h4>Select a Player</h4></div>", unsafe_allow_html=True)
all_batsmen = deliveries['batter'].unique()
selected_player = st.selectbox("", sorted(all_batsmen), key="player_dropdown")

# Filter Player Data
player_data = deliveries[deliveries['batter'] == selected_player]
runs_per_match = player_data.groupby('match_id')['batsman_runs'].sum()

# KPIs
total_runs = player_data['batsman_runs'].sum()
balls_faced = player_data.shape[0]
strike_rate = (total_runs / balls_faced) * 100 if balls_faced else 0

# Display KPIs
st.markdown("### 📊 Player Overview")
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.markdown(f"<div class='kpi-card'>🏏<br><div class='metric-title'>Total Runs</div><h3 style='color: black;'>{total_runs}</h3></div>", unsafe_allow_html=True)
with kpi2:
    st.markdown(f"<div class='kpi-card'>🎯<br><div class='metric-title'>Balls Faced</div><h3 style='color: black;'>{balls_faced}</h3></div>", unsafe_allow_html=True)
with kpi3:
    st.markdown(f"<div class='kpi-card'>⚡<br><div class='metric-title'>Strike Rate</div><h3 style='color: black;'>{round(strike_rate, 2)}</h3></div>", unsafe_allow_html=True)

# Prepare Data for Altair Chart
runs_df = runs_per_match.reset_index()
runs_df.columns = ['Match ID', 'Runs']

# Altair Line Chart
line_chart = alt.Chart(runs_df).mark_line(
    color='#FF4B4B',
    strokeWidth=3
).encode(
    x=alt.X('Match ID:O', title='Match ID'),
    y=alt.Y('Runs:Q', title='Runs Scored'),
    tooltip=['Match ID', 'Runs']
).properties(
    width='container',
    height=300
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
)

# Chart Display
st.markdown(f"<div class='chart-box'><h4 style='color: black;'>📈 {selected_player} - Runs Across Matches</h4>", unsafe_allow_html=True)

st.altair_chart(line_chart, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Optional footer
st.markdown("<br><div style='text-align:center; color:#aaa;'>Data-driven Player Insights 📈</div>", unsafe_allow_html=True)
