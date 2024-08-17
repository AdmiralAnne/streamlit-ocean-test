import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info('A minimal way to take the OCEAN Test and get insights into your personality!')

# Read the CSV with renamed 'score' column (assuming it exists)
df = pd.read_csv("OCEAN_questions - give me the sheet here as a table.csv", names=['question', 'choice'])
df

for index in df['question']:
    q = question['index']
    q

st.success("You've completed the OCEAN Test!")