# Data Engineering Chatbot
# Project Overview

Data-Engineering-Chatbot is a web-based application that allows users to upload datasets (CSV/XLSX) and perform basic data engineering tasks such as data profiling, cleaning, and downloading cleaned data.

# Features
Upload CSV / Excel files
View dataset information (rows, columns, column names)
Detect missing values
Identify duplicate records
Remove duplicates
Download cleaned dataset
# Tech Stack
Python
Pandas
Streamlit (Frontend)
FastAPI (Backend API)
# Workflow

User Upload → Streamlit UI → FastAPI Backend → Data Processing (Pandas) → Cleaned Output Download

# How to Run Locally
1. Clone the repository
git clone https://github.com/jaganmohanreddy1223/Data-Engineering-Chatbot.git
2. Install dependencies
pip install -r requirements.txt
3. Run backend
uvicorn main:app --reload
4. Run frontend
streamlit run app.py

# Future Improvements
Add authentication system.

Store datasets in cloud storage.

Add data visualization dashboard.

Deploy full system on cloud.
