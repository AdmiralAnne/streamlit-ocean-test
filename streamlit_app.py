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


answers = dict_to_dataframe(all_answers)
answers

# Manual calculations for OCEAN scores
extraversion_score = (answers['1'] + answers['3'] + answers['4'] + answers['6'] + answers['8']) - (answers['2'] + answers['5'] + answers['7'] + answers['9'])
neuroticism_score = (answers['10'] + answers['12'] + answers['13'] + answers['15'] + answers['17']) - (answers['11'] + answers['14'] + answers['16'])
openness_score = (answers['19'] + answers['20'] + answers['21'] + answers['23']) - (answers['18'] + answers['22'] + answers['24'] + answers['25'])
agreeableness_score = (answers['27'] + answers['29'] + answers['30'] + answers['32']) - (answers['26'] + answers['28'] + answers['31'] + answers['33'])
conscientiousness_score = (answers['34'] + answers['36'] + answers['39'] + answers['40']) - (answers['35'] + answers['37'] + answers['38'] + answers['41'])

# Display results
st.success("Thank you for completing the test!")
st.subheader("Your OCEAN Scores:")
st.write("Extraversion:", extraversion_score)
st.write("Neuroticism:", neuroticism_score)
st.write("Openness:", openness_score)
st.write("Agreeableness:", agreeableness_score)
st.write("Conscientiousness:", conscientiousness_score)