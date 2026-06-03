import streamlit as st
import pandas as pd
import pickle
import os
import numpy as np

st.set_page_config(page_title="Smart Hospital Patient Navigator", page_icon = "🏥", layout="wide")

st.markdown("""
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {font-family: 'Inter', sans-serif}
    #MainMenu {visibility: hideen;}
    header[data-testid="stHeader"] {display:none;}
  </style>
""")
