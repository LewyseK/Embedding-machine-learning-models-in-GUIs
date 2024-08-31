import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Dashboard",
    page_icon=":chart_line:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Welcome to My Dashboard")
st.write("Add your visualizations")

df =pd.read_csv("./data/train.csv")

st.write("### Gender vs Churn")
Gender_churn = df.groupby('gender')['Churn'].value_counts().unstack()
ax=Gender_churn.plot(kind='bar', figsize=(8, 6))
plt.title('Churn by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=12)
plt.show()

st.write("### Distribution of churn by tenure")

ChurnRate_by_tenure = df.groupby('tenure')['Churn'].value_counts(normalize=True).unstack()
ChurnRate_by_tenure.plot(kind='line', figsize=(12, 5), color=['blue', 'red'])
plt.title('Churn Rate by Tenure')
plt.xlabel('Tenure (in months)')
plt.ylabel('Churn Rate')
plt.xticks(rotation=45, ha='right') 

st.write("Monthly Charges vs Churn")
fig = sns.barplot(data = df, x= 'Churn', y= 'MonthlyCharges')
plt.title('Monthly Charges vs Churn')
st.pyplot(fig)
