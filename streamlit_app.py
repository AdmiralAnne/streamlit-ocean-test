import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info("""
This test offers insights into your traits. 

  * Answer statements using a 1-5 scale (1 = disagree strongly, 5 = agree strongly)
  * No time limit, answer thoughtfully and Honestly.

""")

# Rest of your code for displaying questions...

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

with st.expander("Your Results - Open after all 41 questions only/-"):
    df


import pandas as pd

def calculate_ocean_scores(df):
  """Calculates OCEAN scores based on the provided DataFrame.
  Returns: A dictionary containing the OCEAN scores.
  """

  # Define reverse score questions for each factor
  reverse_questions = {
      'Extraversion': [2, 5, 7, 9],
      'Neuroticism': [11, 14, 16],
      'Openness': [18, 22, 24, 25],
      'Agreeableness': [26, 28, 31, 33],
      'Conscientiousness': [35, 37, 38, 41]
  }

  # Function to calculate scores for a factor
  def calculate_factor_score(factor, df):
    reverse_items = reverse_questions[factor]
    normal_items = [x for x in range(1, df.shape[0] + 1) if x not in reverse_items]

    # Reverse score for reverse items
    df.loc[df['ID'].isin(reverse_items), 'choice'] = 6 - df['choice']

    # Calculate factor score
    factor_score = df[df['factor'] == factor]['choice'].mean()
    return factor_score

  # Calculate scores for each factor
  ocean_scores = {}
  for factor in ['Extraversion', 'Neuroticism', 'Openness', 'Agreeableness', 'Conscientiousness']:
    ocean_scores[factor] = calculate_factor_score(factor, df)

  return ocean_scores

# Example usage:
# Assuming df is your DataFrame with columns 'ID', 'question', 'factor', and 'choice'
ocean_scores = calculate_ocean_scores(df)

# Print the results
for factor, score in ocean_scores.items():
  print(f"Your {factor} score is: {score:.2f}")