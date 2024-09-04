import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 
# st.set_page_config(
    # page_title="Dashboard",
    # page_icon=":chart_line:",
    # layout="wide",
    # initial_sidebar_state="expanded"
# )
def show_dashboard():
    st.title("Welcome to My Dashboard")
    st.write("Add your visualizations")

    df =pd.read_csv("./Data/train.csv")

    st.write("### Gender vs Churn")
    Gender_churn = df.groupby('gender')['Churn'].value_counts().unstack()
    fig,ax=plt.subplots(figsize=(12,5))
    Gender_churn.plot(kind='bar', ax=ax)
    ax.set_title('Churn by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=12)
    st.pyplot(fig)

    st.write("### Distribution of churn by tenure")

    ChurnRate_by_tenure = df.groupby('tenure')['Churn'].value_counts(normalize=True).unstack()
    ChurnRate_by_tenure.plot(kind='line', figsize=(12, 5), color=['blue', 'red'])
    fig,ax=plt.subplots(figsize=(12,5))
# ax.plot(data=ChurnRate_by_tenure,'-', color=['blue', 'red'])
    ax.plot(ChurnRate_by_tenure.index, ChurnRate_by_tenure['Yes'], '-', color='blue')
    ax.set_title('Churn Rate by Tenure')
    ax.set_xlabel('Tenure (in months)')
    ax.set_ylabel('Churn Rate')
    ax.set_xticks(rotation=45, ha='right')
    st.pyplot(fig)
   
    st.write("### Monthly Charges vs Churn")
    fig,ax = plt.subplots(figsize=(12,5))
    sns.barplot(data = df, x= 'Churn', y= 'MonthlyCharges')
    ax.set_title('Monthly Charges vs Churn')
    st.pyplot(fig)

if __name__=="__main__":
    show_dashboard()
