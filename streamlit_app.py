import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info('A minimal way to take the OCEAN Test and get insights into your personality!')

# import the csv dataset and read the file
data=pd.read_csv("OCEAN_questions.csv")
data

questions=data.loc[:, ["ID", "question"]]
questions

st.radio("**Question number 1**", ["1","2","3","4","5"], index=0, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, horizontal=False, captions=[
        "Disagree strongly",
        "Disagree a little",
        "Neither agree nor disagree",
        "Agree a little",
        "Agree strongly"], label_visibility="visible")