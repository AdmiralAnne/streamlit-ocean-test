import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info("""
This test offers insights into your traits. Be honest!

* Answer statements using a 1-5 scale (1 = disagree strongly, 5 = agree strongly)
* There is no time limit, answer thoughtfully.

**Please answer all questions as accurately as possible.**
""")

# Import the CSV dataset and read the file
try:
  data = pd.read_csv("OCEAN_questions.csv")
  questions = data.loc[:, ["ID", "question", "choice"]]
except FileNotFoundError:
  st.error("Error: 'OCEAN_questions.csv' file not found. Please ensure the file exists in the same directory as your script.")
  exit()


# Display questions with radio buttons
all_answers = {}
for index, row in questions.iterrows():
  question_id = row['ID']
  question_text = row['question']
  answer = st.radio(f"Question {question_id}: {question_text}", options=[1, 2, 3, 4, 5],
                     captions=[
                         "Disagree strongly",
                         "Disagree a little",
                         "Neither agree nor disagree",
                         "Agree a little",
                         "Agree strongly"
                     ],
                     horizontal=False, key=question_id)
  all_answers[question_id] = answer

questions
data
all_answers

def dict_to_dataframe(data_dict):
  """Converts a dictionary to a Pandas DataFrame.

  Args:
    data_dict: A dictionary where keys are question IDs and values are answers.

  Returns:
    A Pandas DataFrame with 'ID' and 'answer' columns.
  """

  # Convert the dictionary to a list of tuples
  data = [(k, v) for k, v in data_dict.items()]

  # Create a DataFrame from the list of tuples
  df = pd.DataFrame(data, columns=['ID', 'answer'])

  return df


answers_df = dict_to_dataframe(all_answers)
answers_df


# Manual calculations for OCEAN scores
extraversion_score = (answers_df[answers_df['ID'].isin([1, 3, 4, 6, 8])]['answer'].sum() -
                       answers_df[answers_df['ID'].isin([2, 5, 7, 9])]['answer'].sum())

neuroticism_score = (answers_df[answers_df['ID'].isin([10, 12, 13, 15, 17])]['answer'].sum() -
                       answers_df[answers_df['ID'].isin([11, 14, 16])]['answer'].sum())

openness_score = (answers_df[answers_df['ID'].isin([19, 20, 21, 23])]['answer'].sum() -
                   answers_df[answers_df['ID'].isin([18, 22, 24, 25])]['answer'].sum())

agreeableness_score = (answers_df[answers_df['ID'].isin([27, 29, 30, 32])]['answer'].sum() -
                       answers_df[answers_df['ID'].isin([26, 28, 31, 33])]['answer'].sum())

conscientiousness_score = (answers_df[answers_df['ID'].isin([34, 36, 39, 40])]['answer'].sum() -
                           answers_df[answers_df['ID'].isin([35, 37, 38, 41])]['answer'].sum())

# Display results
st.success("Thank you for completing the test!")
st.subheader("Your OCEAN Scores:")
st.write("Extraversion:", extraversion_score)
st.write("Neuroticism:", neuroticism_score)
st.write("Openness:", openness_score)
st.write("Agreeableness:", agreeableness_score)
st.write("Conscientiousness:", conscientiousness_score)

st.info(""" 

General Interpretations for OCEAN Traits

Extraversion:
High Scores (16-21): Outgoing, sociable, assertive, enthusiastic, and enjoys being the center of attention.
Average Scores (6-15): Balanced between introversion and extraversion, with a mix of social and solitary tendencies.
Low Scores (-15 to 5): Introverted, reserved, quiet, and prefers solitary activities or small groups.

Neuroticism:
High Scores (16-21): Prone to anxiety, moodiness, irritability, and emotional instability.
Average Scores (6-15): Experiencing a moderate level of emotional fluctuations and stress.
Low Scores (-15 to 5): Calm, relaxed, emotionally stable, and resilient to stress.

Openness:
High Scores (16-21): Curious, imaginative, intellectual, open to new experiences, and appreciates art and creativity.
Average Scores (6-15): Moderate levels of curiosity and openness to new ideas.
Low Scores (-15 to 5): Practical, conventional, and prefers routine and familiar experiences.

Agreeableness:
High Scores (16-21): Cooperative, trusting, empathetic, and considerate of others.
Average Scores (6-15): Balanced between cooperation and assertiveness.
Low Scores (-15 to 5): Competitive, suspicious, and assertive, with a focus on personal goals.

Conscientiousness: 
High Scores (16-21): Organized, disciplined, reliable, and hardworking.
Average Scores (6-15): Moderately organized and reliable.
Low Scores (-15 to 5): Spontaneous, careless, and less focused on goals.

""")