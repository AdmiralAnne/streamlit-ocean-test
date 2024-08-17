import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info('A minimal way to take the OCEAN Test and get insights into your personality!')

df=pd.read_csv("OCEAN_questions - give me the sheet here as a table.csv")

def display_questions(df):
  """Displays questions with radio buttons for answers using Streamlit.

  Args:
    df: The DataFrame containing question data.

  Returns:
    The modified DataFrame with user choices.
  """

  for index, row in df.iterrows():
    question = row['question']
    st.subheader(f"Question {index + 1}: {question}")

    # Display answer options with radio buttons
    answer = st.radio("Choose your answer:", options=[1, 2, 3, 4, 5])
    df.loc[index, 'choice'] = answer

  return df

# Assuming you have a DataFrame named 'df' with the provided data
# Create a 'choice' column if it doesn't exist

df = display_questions(df)
st.success("Questionnaire completed!")