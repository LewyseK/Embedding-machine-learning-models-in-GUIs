import streamlit as st
import joblib
from sklearn import pipeline
import pandas as pd
import numpy as np
import os
import datetime

st.set_page_config(
    page_title="Predictions",
    Page_icon=":siren:",
    layout="wide",
    initial_sidebar_state="expanded"    
)

st.title("Make Predictions")
st.write("Get predicive insights")

st.cache_resource(show_spinner="models loading....")
def random_forest_pipeline():
    pipeline= joblib.load("./models/Random_forest.joblib")
    return pipeline