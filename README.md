# 🏏 IPL Dashboard - Data-Driven Cricket Insights

The **IPL Dashboard** is an interactive web application built using **Streamlit** that transforms IPL data into compelling visuals and actionable insights. Whether you're a cricket enthusiast, data analyst, or just curious about IPL trends, this dashboard offers an engaging way to explore player performances, team strategies, venue statistics, and more.

## 📁 Dataset

This project uses the **IPL Complete Dataset (2008–2024)**, available on Kaggle:

🔗 [Download Dataset from Kaggle](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)

> ⚠️ Make sure to place the following CSV files inside a folder named `data/`:
- `matches.csv`
- `deliveries.csv`

## 🚀 Features

### 1. IPL Season Overview
- Quick KPIs like total matches, seasons, and teams.
- Matches per season breakdown.
- Top teams and players based on wins and awards.

### 2. Team Strategy Insights
- Toss decisions and their win conversion rates.
- Batting strategy effectiveness based on match results.

### 3. Venue Insights
- Venue-based average win margins.
- Top-performing teams at each venue.

### 4. Player Performance
- Individual batting stats such as strike rate, runs, and balls faced.
- Match-wise performance trends.

### 5. Player Comparison
- Head-to-head comparison of key batting stats between two players.

### 6. Season-wise Team Performance
- Year-by-year breakdown of wins and losses for any selected team.

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python (Pandas, Altair, Plotly)  
- **Visualization**: Plotly, Altair, Streamlit Charts  
- **Deployment Ready**: Easily deployable to platforms like Streamlit Cloud or Render

## 💻 How to Run Locally

1. **Clone the Repository, Install Dependencies & Run the App**

Make sure you have Python 3.8+ installed. Then follow these steps:

```bash
# Clone the repository
git clone https://github.com/sangamithrasaravanan123/IPL-Dashboard.git
cd IPL-Dashboard

# (Optional) Create and activate a virtual environment
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install required libraries
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py
