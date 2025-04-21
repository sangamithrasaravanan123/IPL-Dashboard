🏏 IPL Dashboard - Data-Driven Cricket Insights
IPL Dashboard, an interactive web application built using Streamlit that transforms IPL data into compelling visuals and actionable insights. Whether you're a cricket enthusiast, data analyst, or just curious about IPL trends, this dashboard offers an engaging way to explore player performances, team strategies, venue statistics, and more.

📁 Dataset
This project uses the IPL Complete Dataset (2008–2024), available on Kaggle:

🔗 Download Dataset from Kaggle
https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020

Make sure to place the following CSVs inside a folder named data:
matches.csv
deliveries.csv

🚀 Features
IPL Season Overview: Quick KPIs, matches per season, top teams, and players.

Team Strategy Insights: Toss decisions, win conversion rates, and batting strategy effectiveness.

Venue Insights: Venue-based average win margins and top-performing teams.

Player Performance: Individual batting stats with strike rate, runs, and match-wise performance trends.

Player Comparison: Head-to-head comparison of key batting stats between two players.

Season-wise Team Performance: Year-by-year wins and losses for any team.



🛠️ Tech Stack
Frontend: Streamlit

Backend: Python (Pandas, Altair, Plotly)

Visualization: Plotly, Altair, Streamlit Charts

Deployment Ready: Easily deployable to platforms like Streamlit Cloud or Render


💻 How to Run Locally
Clone the repository
git clone https://github.com/sangamithrasaravanan123/IPL-Dashboard.git

cd IPL-Dashboard

Install dependencies
Make sure you have Python 3.8+ installed. Then, create a virtual environment (optional) and install packages:

pip install -r requirements.txt

Add Dataset
Download the dataset from Kaggle (linked above), and place matches.csv and deliveries.csv in a folder named data.

STRUCTURE
IPL-Dashboard/
├── data/
│   ├── matches.csv
│   └── deliveries.csv
├── streamlit_app.py
└── pages/
     |__ 1_Overview.py
     |__ ....

Run the App
streamlit run streamlit_app.py

License
This project is licensed under the MIT License. Feel free to fork, modify, and contribute.