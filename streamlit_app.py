import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info('A minimal way to take the OCEAN Test and get insights into your personality!')

# import the csv dataset and read the file
data=pd.read_csv("OCEAN_questions.csv")
questions=data.loc[:, ["ID", "question","choice"]]

with st.expander("Data"):
    data
    questions

def display_questions(df):
  """Displays questions one by one with radio buttons for answers and stores choices in DataFrame.
    Returns: The modified DataFrame with user choices stored.
  """

  if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

  if st.session_state.current_question < len(df):
    current_question = st.session_state.current_question
    question_id = df.loc[current_question, 'ID']
    question_text = df.loc[current_question, 'question']
    st.subheader(f"Question {question_id}: {question_text}")

    answer = st.radio("Choose your answer:", options=[1, 2, 3, 4, 5], index=0, key=current_question,
                       captions=[
                           "Disagree strongly",
                           "Disagree a little",
                           "Neither agree nor disagree",
                           "Agree a little",
                           "Agree strongly"
                       ],
                       horizontal=False)
    df.loc[current_question, 'choice'] = answer

    if st.button('Next'):
      st.session_state.current_question += 1

  return df

df = display_questions(questions.copy())  # Avoid modifying original DataFrame
df