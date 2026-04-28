import streamlit as st

#Title of app
st.title("My First Streamlit App")
#Adding Text
st.write("Hello! Creating a simple web application using streamlit library")

#Text Input
name=st.text_input("Enter your name:")
#Number Input
age=st.number_input("Enter your age:")
#Display a message when button is clicked
if st.button("Submit"):
    st.write("Hello,{name}! Welcome to streamlit.") 
