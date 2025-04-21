import streamlit as st
import pandas as pd

# Load dataset
matches = pd.read_csv("data/matches.csv")

# Page config
st.set_page_config(page_title="IPL Season Overview", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .page-title {
            font-size: 48px;
            font-weight: 800;
            color: white;
            text-align: center;
            margin-bottom: 10px;
        }
        .highlight-box {
            background: #fefefe;
            border: 2px solid #FF4B4B;
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
            font-size: 20px;
            font-weight: 600;
            color: #333;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        .section-title {
            font-size: 28px;
            font-weight: 700;
            color: gray;
            margin-top: 40px;
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
        .star-table th, .star-table td {
            padding: 8px 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="page-title">📊 IPL Season Overview</div>', unsafe_allow_html=True)
st.markdown("### 🏏 Quick Highlights")

# KPI Cards
total_matches = matches.shape[0]
total_seasons = matches['season'].nunique()
total_teams = matches['team1'].nunique()

kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.markdown(f"<div class='highlight-box'>🧮 Total Matches<br>{total_matches}</div>", unsafe_allow_html=True)
with kpi2:
    st.markdown(f"<div class='highlight-box'>📆 Seasons Played<br>{total_seasons}</div>", unsafe_allow_html=True)
with kpi3:
    st.markdown(f"<div class='highlight-box'>👥 Participating Teams<br>{total_teams}</div>", unsafe_allow_html=True)

# Matches per Season
st.markdown("<div class='section-title'>📅 Matches per Season</div>", unsafe_allow_html=True)
season_summary = matches['season'].value_counts().sort_index()
st.bar_chart(season_summary)

# Top 5 teams by wins
st.markdown("<div class='section-title'>🏆 Top 5 Teams by Wins</div>", unsafe_allow_html=True)
top_teams = matches['winner'].value_counts().head(5)

st.markdown("<div class='team-strip'>", unsafe_allow_html=True)
for team, wins in top_teams.items():
    st.markdown(f"<div class='team'>🏏 {team}<br>🏆 {wins} Wins</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Player of the Match Table
st.markdown("<div class='section-title'>⭐ Top 'Player of the Match' Award Winners</div>", unsafe_allow_html=True)
top_players = matches['player_of_match'].value_counts().head(5).reset_index()
top_players.columns = ['Player', 'Awards']
st.table(top_players)

# Optional footer
st.markdown("<br><div style='text-align:center; color:#aaa;'>Data-driven IPL insights, one stat at a time 📈</div>", unsafe_allow_html=True)
