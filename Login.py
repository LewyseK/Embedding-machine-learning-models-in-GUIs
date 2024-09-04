import streamlit as st
import bcrypt

def hash_password(password:str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(stored_password: bytes,password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), stored_password)

credentials = {
    "usernames": {
        "thejoker": {
            "name": "The Joker",
            "password": hash_password("password123"),
        },
        "shejoker":{
            "name": "She Joker",
            "password": hash_password("password456"),
        }
    }
}

def authenticate(username,password):
    if username in credentials["usernames"]:
        stored_password = credentials["usernames"][username]["password"]
        if verify_password(stored_password, password):
            return True
    return False

def show_login():
    st.sidebar.title("Login")

    with st.sidebar.form(key="Login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            if authenticate(username, password):
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success("Login successfull")    
            else:
                st.sidebar.error("Invalid credentials.Username or Password incorrect Please try again.")
                