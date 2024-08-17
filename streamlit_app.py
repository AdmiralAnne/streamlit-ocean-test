import streamlit as st
import pandas as pd
st.title('OCEAN Test App')

st.info('A minimal way to take the OCEAN Test and get insights into your personality!')
df=pd.read_csv("OCEAN_questions - give me the sheet here as a table.csv")
df = df.rename(columns={'score': 'choice'})
df