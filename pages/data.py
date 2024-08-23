import streamlit as st
import pandas as pd
st.title("This is the Data Page")
#Load data

@st.cache(persist=True)
def load_data():
    data = pd.read_csv('New_Test_data.csv')
    return data

st.dataframe(load_data())