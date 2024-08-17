import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info('A minimal way to take the OCEAN Test and get insights into your personality!')

# import the csv dataset and read the file
data=pd.read_csv("OCEAN_questions.csv")
data

questions=data['ID','question']
questions