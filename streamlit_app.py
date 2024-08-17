import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info('A minimal way to take the OCEAN Test and get insights into your personality!')

# Read the CSV with renamed 'score' column (assuming it exists)
df = pd.read_csv("OCEAN_questions - give me the sheet here as a table.csv", names=['question', 'choice'])


for index, row in df.iterrows():
    question = row['question']
    choice_text = st.radio(f"Questionndex+1: {question}",("1. Disagree strongly",
                             "2. Disagree a little",
                             "3. Neither agree nor disagree",
                             "4. Agree a little",
                             "5. Agree strongly"))
    df.loc[index, 'choice'] = int(choice_text[0])  # Extract the number directly

df = create_questionnaire(df.copy())  # Avoid modifying original dataframe
st.success("You've completed the OCEAN Test!")