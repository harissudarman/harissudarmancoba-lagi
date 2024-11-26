#!/bin/bash
gunicorn endpoint:app --bind 0.0.0.0:10000 &
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
