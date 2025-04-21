import streamlit as st
import pandas as pd

# Load matches dataset
matches = pd.read_csv("data/matches.csv")

# Page config
st.set_page_config(page_title="🏟️ Venue Insights", layout="wide")

# Custom CSS Styling
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
st.markdown("<div class='page-title'>🏟️ Venue Insights</div>", unsafe_allow_html=True)

# Venue Selection
venues = matches['city'].unique()
selected_venue = st.selectbox("Select a Venue", sorted([str(v) for v in venues]))

# Filter matches for selected venue
venue_data = matches[matches['city'] == selected_venue]
avg_score = venue_data['result_margin'].mean()

# Display average win margin for the venue
st.markdown("<div class='highlight-box'>📊 <div class='metric-title'>Average Win Margin (Runs)</div><h3 style='color: black;'>{:.2f}</h3></div>".format(avg_score), unsafe_allow_html=True)

# Display top 3 winning teams at the venue
top_winning_teams = venue_data['winner'].value_counts().head(3)
st.markdown("<div class='section-title'>🏆 Most Successful Teams at This Venue</div>", unsafe_allow_html=True)

# Bar chart for top winning teams
st.markdown("<div class='chart-box'>", unsafe_allow_html=True)
st.bar_chart(top_winning_teams)
st.markdown("</div>", unsafe_allow_html=True)

# Optional footer
st.markdown("<br><div style='text-align:center; color:#aaa;'>Data-driven Venue Insights, enhancing team strategy 📈</div>", unsafe_allow_html=True)
