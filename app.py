import streamlit as st

st.set_page_config(
    page_title="Classification App",
    page_icon=":trendline:",
    layout="wide"
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
                
""")
st.subheader("App features")
st.markdown("""
- **View Data** : Access proprietory data
- **Dashboard** : Interactive data visualizations for insights.        

""")