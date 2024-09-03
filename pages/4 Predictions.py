import streamlit as st
import joblib
from sklearn import pipeline
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import os
import datetime

st.set_page_config(
    page_title="Predictions",
    page_icon=":siren:",
    layout="wide",
    initial_sidebar_state="expanded"    
)

st.title("Make Predictions")
st.subheader("Decisions with data-driven insights")

@st.cache_resource(show_spinner="model loading....")
def random_forest_pipeline():
    pipeline= joblib.load("./models/Random_forest.joblib")
    return pipeline

@st.cache_resource(show_spinner="model loading....")
def SVC_pipeline():
    pipeline= joblib.load("./models/SVC_model.joblib")
    return pipeline

l_encoder = LabelEncoder()
def select_model():
    col1, col2,= st.columns(2)

    with col1:
         st.selectbox("Select a model", ["Random Forest", "Support Vector Classifier"],key="selected_model")
    with col2:
        pass
    if st.session_state["selected_model"] == "Random Forest":
            pipeline = random_forest_pipeline()
    else:
        pipeline = SVC_pipeline()

    encoder= joblib.load("./models/Encoder.joblib")

    return pipeline, encoder

if "prediction" not in st.session_state:
    st.session_state["prediction"] = None
    
if "probability" not in st.session_state:
    st.session_state["probability"] = None 


def make_prediction(pipeline,encoder):
     gender=st.session_state["gender"] 
     SeniorCitizen=st.session_state["SeniorCitizen"]
     Partner=st.session_state["Partner"]
     Dependents=st.session_state["Dependents"]
     tenure=st.session_state["tenure"]
     PhoneService=st.session_state["PhoneService"]
     MultipleLines=st.session_state["MultipleLines"]
     InternetService=st.session_state["InternetService"]
     OnlineSecurity=st.session_state["OnlineSecurity"]
     OnlineBackup=st.session_state["OnlineBackup"]
     DeviceProtection=st.session_state["DeviceProtection"]
     TechSupport=st.session_state["TechSupport"]
     StreamingTV=st.session_state["StreamingTV"]
     StreamingMovies=st.session_state["StreamingMovies"]
     Contract=st.session_state["Contract"]
     PaperlessBilling=st.session_state["PaperlessBilling"]
     PaymentMethod=st.session_state["PaymentMethod"]
     MonthlyCharges=st.session_state["MonthlyCharges"]
     TotalCharges=st.session_state["TotalCharges"]
     

     columns = ["gender","SeniorCitizen","Partner","Dependents","tenure","PhoneService","MultipleLines",
                "InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV",
                "StreamingMovies","Contract","PaperlessBilling","PaymentMethod","MonthlyCharges","TotalCharges"] 

     data = {"gender":[gender],"SeniorCitizen":[SeniorCitizen],"Partner":[Partner],"Dependents":[Dependents],"tenure":[tenure],
             "PhoneService":[PhoneService],"MultipleLines":[MultipleLines],"InternetService":[InternetService],"OnlineSecurity":[OnlineSecurity],
             "OnlineBackup":[OnlineBackup],"DeviceProtection":[DeviceProtection],"TechSupport":[TechSupport],"StreamingTV":[StreamingTV],
             "StreamingMovies":[StreamingMovies],"Contract":[Contract],"PaperlessBilling":[PaperlessBilling],"PaymentMethod":[PaymentMethod],
             "MonthlyCharges":[MonthlyCharges],"TotalCharges":[TotalCharges]}      
     
     df= pd.DataFrame(data,columns=columns)

     df["Prediction Time"] = datetime.date.today()
     df["Model Used"] = st.session_state["selected_model"]



     df.to_csv("./data/history.csv", mode="a",header=not os.path.exists("./data/history.csv"),index=False)

     pred = pipeline.predict(df)
     pred = int(pred[0])
     prediction = encoder.inverse_transform([pred])

     probability = pipeline.predict_proba(df)

     st.session_state["prediction"] = prediction
     st.session_state["probability"] = probability

     return prediction,probability

def display_form():
    pipeline, encoder= select_model()

    with st.form("input_feature"):
        col1, col2,col3 = st.columns(3)

        with col1:
            st.write("### Demographic Information ###")
            st.selectbox("gender",[
                    "Male","Female"], key="gender")
            st.number_input("SeniorCitizen",
                   min_value = 0, max_value = 1,key="SeniorCitizen")
            st.selectbox("Partner",[
                    "Yes","No"],key = "Partner")
            st.selectbox("Dependents",[
                    "Yes","No"],key = "Dependents")
               
        with col2:
            st.write("### Charges and contract information ###")
            st.number_input("tenure",
                   min_value = 0, max_value = 72, key="tenure")
            st.selectbox("Contract",[
                    "Month-to-Month","One year","two year"], key="Contract")
            st.selectbox("Paperless Billing",[
                "Yes","No"], key="PaperlessBilling")
            st.number_input("monthly charges",
                    min_value=18, max_value=119,key="MonthlyCharges")
            st.number_input("total charges",
                    min_value=18, max_value=8700,key= "TotalCharges")
               
        with col3:
            st.write("### Packages and Additional services ###")
            st.selectbox("PhoneService",[
                    "Yes","No"], key="PhoneService")
            st.selectbox("MultipleLines",[
                    "Yes","No"], key="MultipleLines")
            st.selectbox("InternetService",[
                    "DSL","Fiber optic","No"], key="InternetService")
            st.selectbox("OnlineSecurity",[
                    "Yes","No"], key="OnlineSecurity")
            st.selectbox("OnlineBackup",[
                    "Yes","No"], key="OnlineBackup")
            st.selectbox("DeviceProtection",[
                    "Yes","No"], key="DeviceProtection")
            st.selectbox("TechSupport",[
                    "Yes","No"], key="TechSupport")
            st.selectbox("StreamingTV",[
                    "Yes","No"], key="StreamingTV")
            st.selectbox("StreamingMovies",[
                    "Yes","No"], key="StreamingMovies") 
            st.selectbox("PaymentMethod",[
                    "Electronic check","Mailed check","Bank transfer (automatic)",
                    "Credit card (automatic)"], key="PaymentMethod")   


        st.form_submit_button("Make Prediction", on_click=make_prediction,kwargs=dict(
                    pipeline=pipeline,encoder=encoder))
        

if __name__ =="__main__":
    st.title("Make a Prediction")
    display_form()

    prediction  = st.session_state['prediction']
    probability = st.session_state['probability']

    if not prediction:
        st.markdown("### Predictions will show here")
    elif prediction == "Yes":
        probability_of_yes = probability[0][1] * 100
        st.markdown(f"### The employee will leave the company with a probability of {round(probability_of_yes,2)}%")
        
    else:
        probability_of_no = probability[0][0] * 100
        st.markdown(f"### The employee will leave the company with a probability of {round(probability_of_no,2)}%")
        

    #st.write(st.session_state)


     
              
            
            
            
            
                

               
               
               
               
               
               
                    
                           
               


            




