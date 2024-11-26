#!/bin/bash
# Jalankan Flask API di latar belakang
gunicorn endpoint:app --bind 0.0.0.0:10000 &

# Jalankan Streamlit
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
