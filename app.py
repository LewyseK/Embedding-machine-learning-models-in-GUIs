import streamlit as st
import Login
import Dashboard, Data, Predictions,history

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# if "username" not in st.session_state:
    # st.session_state["username"] = None

def check_authentication():
    return st.session_state.get("authenticated", False)

def logout():
    st.session_state["authenticated"]= False
    st.session_state.pop("username", None)
    st.session_state["page"] = "Login"

def main():
    if check_authentication():
        if "page" not in st.session_state:
            st.session_state["page"] = "Home"

        st.sidebar.title(f"Welcome,{st.session_state['username']}")
        if st.sidebar.button("Logout"):
           logout()

        st.sidebar.title("Navigation")
        st.session_state["page"] = st.sidebar.selectbox("Select Page",["Home","Dashboard","Data","Predictions","Prediction History"])

        if st.session_state["page"] == "Home":
            show_home_page()
        elif st.session_state["page"] == "Dashboard":
            Dashboard.show_dashboard()
        elif st.session_state["page"] == "Data":
            Data.load_data()
        elif st.session_state["page"] == "Predictions":
            Predictions.display_form()
        elif st.session_state["page"] == "Prediction History":
            history.history_page()
    else:
        Login.show_login()

        # st.markdown("Customer Churn Prediction App")
        # Create a new column
        

    # Display the image in the new column
        # st.image("./Images/Tel.webp")
        Bg_image = '''
        <style>
        .stApp {
        background-image: url("./Images/Tel.webp");
        background-size: contain;
        background-position: center;
        }
        </style>
        '''
        st.markdown(Bg_image, unsafe_allow_html=True)
# st.set_page_config(
    # page_title="Classification App",
    # page_icon=":trendline:",
    # layout="wide",
    # initial_sidebar_state="expanded"
# )
def show_home_page():
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

    st.subheader("Need any help?")
    st.markdown("Contact")
    st.markdown("For engagements, write & contact us at [lewykk2011@gmail.com]")
    st.button("repository on github", help="Visit Github repository")
    st.write("Visit Github repository at: LewyseKK")
    
if __name__=="__main__":
    main()    