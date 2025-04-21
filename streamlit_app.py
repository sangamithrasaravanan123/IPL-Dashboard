import streamlit as st

# Page config
st.set_page_config(page_title="IPL Dashboard", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .main-title {
            font-size: 60px;
            font-weight: 800;
            color: white;
            text-align: center;
            margin-top: 30px;
            margin-bottom: 0;
        }
        .subtext {
            text-align: center;
            font-size: 20px;
            color: #555;
            margin-bottom: 30px;
        }
        .info-box {
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            border-left: 5px solid #FF4B4B;
            padding: 1.2rem;
            border-radius: 10px;
            font-size: 17px;
            color: #333;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.05);
            margin: auto;
            width: 85%;
            text-align: center;
            margin-bottom: 40px;
        }
        .banner {
            position: relative;
            margin-top: 20px;
        }
        .banner img {
            width: 100%;
            border-radius: 16px;
            box-shadow: 0px 5px 25px rgba(0,0,0,0.2);
        }
        hr.custom-hr {
            border: none;
            height: 2px;
            background: #FF4B4B;
            width: 10%;
            margin: 0 auto 40px auto;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<div class="main-title">IPL PERFORMANCE & STRATEGY DASHBOARD</div>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Dive deep into IPL matches, player performances, and team strategies. Use the sidebar to explore different pages.</p>', unsafe_allow_html=True)
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)

# Full-width Info Box
st.markdown('<div class="info-box">📊 <strong>Navigate through the sidebar</strong> to view key statistics: Overview, Player Insights, Team Strategy, and Venue Analysis. Uncover patterns and insights to make data-driven predictions and analyses.</div>', unsafe_allow_html=True)

# Banner at the bottom
st.image("images/ipl_banner.jpeg", use_container_width=True)

# Footer
st.markdown("""
    <br>
    <div style='text-align: center; color: #aaa; font-size: 14px;'>
        Made with ❤️ for cricket fans | Powered by Streamlit
    </div>
""", unsafe_allow_html=True)
