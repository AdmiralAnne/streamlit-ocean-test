import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info('A minimal way to take the OCEAN Test and get insights into your personality!')

# import the csv dataset and read the file
data=pd.read_csv("OCEAN_questions.csv")
data

questions=data.loc[:, ["ID", "question","choice"]]
questions

# st.radio("**Question number 1**", ["1","2","3","4","5"], index=0, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, horizontal=False, captions=[
#        "Disagree strongly",
#        "Disagree a little",
#        "Neither agree nor disagree",
#        "Agree a little",
#        "Agree strongly"], label_visibility="visible")


import streamlit as st
import pandas as pd

def display_questions(df):
  """Displays questions with radio buttons for answers and stores choices in DataFrame.

  Args:
    df: The DataFrame containing question data (ID, question, choice).

  Returns:
    The modified DataFrame with user choices stored.
  """

  for index, row in df.iterrows():
    question_id = row['ID']
    question_text = row['question']
    st.subheader(f"Question {question_id}: {question_text}")

    # Display answer options with radio buttons (unique key)
    answer = st.radio("Choose your answer:", options=[1, 2, 3, 4, 5],Index=None,key=index,
                       captions=[
                           "Disagree strongly",
                           "Disagree a little",
                           "Neither agree nor disagree",
                           "Agree a little",
                           "Agree strongly"
                       ],
                       horizontal=False)
    df.loc[index, 'choice'] = answer

  return df

# Assuming you already have the 'questions' DataFrame with ID, question, and choice columns

df = display_questions(questions.copy())  # Avoid modifying original DataFrame
st.success("Questionnaire completed!")
df