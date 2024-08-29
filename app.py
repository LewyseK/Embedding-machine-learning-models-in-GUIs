import streamlit as st

st.set_page_config(
    page_title="Classification App",
    page_icon=":trendline:",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Customer churn Prediction App")
st.markdown("""
         This app uses machine learning to predict if a customer will churn or not

   """)
st.subheader("Key features")
st.markdown("""
    1. Upload your dataset
    2. Choose the target variable
    3. Choose the features to use for prediction
    4. Train and evaluate the model
    5. Visualize the results
    6. Deploy the model for predictions
    7. Get a comprehensive report on model performance.        
                
""")
st.subheader("App features")
st.markdown("""
- **Data** : Access data.
- **Dashboard** : Interactive data visualizations for insights.        
- **Predictions** : Get predictions
""")

st.sidebar.write("Need any help?")
st.markdown("Contact")
st.markdown("For engagements, write & contact us at [lewykk2011@gmail.com]")
if st.button("repository on github", help="Visit Github repository"):
    st.write("Visit Github repository at: LewyseKK")
    