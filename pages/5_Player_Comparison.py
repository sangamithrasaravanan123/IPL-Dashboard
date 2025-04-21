import streamlit as st
import pandas as pd

# Load deliveries data
deliveries = pd.read_csv("data/deliveries.csv")

# Page Config
st.set_page_config(page_title="Player Comparison", layout="wide")

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
        .comparison-section {
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
        .metric-title {
            font-size: 22px;
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
        }
        .comparison-box {
            background-color: #fff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(0,0,0,0.04);
            margin-top: 40px;
            text-align: center;
        }
        .comparison-box h3 {
            color: #333;
            font-weight: 700;
            margin-bottom: 20px;
        }
        .comparison-box .metric-value {
            font-size: 24px;
            font-weight: 600;
            color: #FF4B4B;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='page-title'>🆚 Player Comparison</div>", unsafe_allow_html=True)

# Select players for comparison
all_batsmen = deliveries['batter'].unique()
player1 = st.selectbox("Select Player 1", sorted(all_batsmen))
player2 = st.selectbox("Select Player 2", sorted(all_batsmen))

# Filter data for selected players
player1_data = deliveries[deliveries['batter'] == player1]
player2_data = deliveries[deliveries['batter'] == player2]

# Calculate key metrics
player1_runs = player1_data['batsman_runs'].sum()
player2_runs = player2_data['batsman_runs'].sum()

player1_balls = player1_data.shape[0]
player2_balls = player2_data.shape[0]

player1_sr = (player1_runs / player1_balls) * 100 if player1_balls else 0
player2_sr = (player2_runs / player2_balls) * 100 if player2_balls else 0

# Display Comparison Section with Enhanced Layout
st.markdown("<div class='comparison-section'><h3>📊 Comparing {}</h3></div>".format(f"{player1} vs {player2}"), unsafe_allow_html=True)

kpi1, kpi2 = st.columns(2)
with kpi1:
    st.markdown(f"<div class='kpi-card'>🏏<br><div class='metric-title'>Total Runs</div><h3 style='color: black;'>{player1_runs} vs {player2_runs}</h3></div>", unsafe_allow_html=True)

with kpi2:
    st.markdown(f"<div class='kpi-card'>⚡<br><div class='metric-title'>Strike Rate</div><h3 style='color: black;'>{round(player1_sr, 2)} vs {round(player2_sr, 2)}</h3></div>", unsafe_allow_html=True)

# Comparison Box for better visibility
st.markdown("""
    <div class="comparison-box">
        <h3>📈 Performance Comparison</h3>
        <div class="metric-value">
            <p>{} - Total Runs: <strong>{}</strong></p>
            <p>{} - Total Runs: <strong>{}</strong></p>
            <p>{} - Strike Rate: <strong>{:.2f}</strong></p>
            <p>{} - Strike Rate: <strong>{:.2f}</strong></p>
        </div>
    </div>
""".format(player1, player1_runs, player2, player2_runs, player1, player1_sr, player2, player2_sr), unsafe_allow_html=True)

# Optional footer
st.markdown("<br><div style='text-align:center; color:#aaa;'>Player comparison made simple 📊</div>", unsafe_allow_html=True)
