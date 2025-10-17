import streamlit as st

import subprocess

import sys

import os
# Configure the app

st.set_page_config(

    page_title="Vocabulary Builder - App Selector",

    page_icon="🎓",

    layout="wide"

)

st.title("🎓 Vocabulary Builder - App Selector")

st.write("Select an app to launch:")

apps = ["Basic Vocabulary Builder", "Advanced Vocabulary Builder", "Custom Vocabulary Builder"]


selected_app = st.sidebar.radio("Select App", apps)

if selected_app == "Basic Vocabulary Builder":
    st.write("Launching Basic Vocabulary Builder...")
    subprocess.Popen([sys.executable, "app_basic.py"])
    
elif selected_app == "Advanced Vocabulary Builder":
    st.write("Launching Advanced Vocabulary Builder...")
    subprocess.Popen([sys.executable, "app_advanced1.py"])
    
elif selected_app == "Custom Vocabulary Builder":
    st.write("Launching Custom Vocabulary Builder...")
    subprocess.Popen([sys.executable, "app_advanced2.py"])