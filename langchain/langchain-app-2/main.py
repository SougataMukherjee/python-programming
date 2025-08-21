import langchain_helper as lch
import streamlit as st

st.title("Name Generator")

sp_type = st.sidebar.selectbox("What is your name?", ("man", "cat", "dog"))

if sp_type == "man":
    food_type = st.sidebar.text_input("What food do you like?")
elif sp_type == "cat":
    food_type = st.sidebar.text_input("What food does your cat like?")
elif sp_type == "dog":
    food_type = st.sidebar.text_input("What food does your dog like?")

if food_type:
    response = lch.generate_name(sp_type, food_type)
    st.success(response)  
