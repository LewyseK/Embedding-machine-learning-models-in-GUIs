import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Prediction History",
    page_icon=":history:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# st.header("Prediction History")
# if "history"  in st.session_state and not st.session_state.history.empty:
    # st.write(st.session_state.history)
# else:
    # st.write("No prediction history available.")

def history_page():
    st.title("Prediction History")
    data = pd.read_csv("./Data/history.csv")
    st.dataframe(data)

if __name__== '__main__':
    history_page()