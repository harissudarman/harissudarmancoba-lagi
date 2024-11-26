#!/bin/bash
# Jalankan Streamlit di port 8501
streamlit run app.py --server.port 8501 --server.address 0.0.0.0

# Jalankan Flask API di background pada port 10000
gunicorn endpoint:app --bind 0.0.0.0:10000 

