import streamlit as st
import pandas as pd
st.title("This is the Data Page")
#Load data

@st.cache_data(persist=True)
def load_data():
    df=pd.read_csv("Data/train.csv")
    st.dataframe(df.head(10))
    st.write("### Summary statistics")
    st.write(df.describe())

    return df

st.dataframe(load_data())

# df=pd.read_csv("Data/train.csv")
# st.dataframe(df.head(10))
# st.write("### Summary statistics")
# st.write(df.describe())

