import streamlit as st
from gui.dashboard import render_dashboard

st.set_page_config(page_title="RetroAI Prototype 2", layout="wide")

st.markdown("<h1 style='text-align:center; color:#00ffee;'>🎮 RetroAI – Prototype 2</h1>", unsafe_allow_html=True)
render_dashboard()
