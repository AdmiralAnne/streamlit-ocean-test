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


import pandas as pd

def calculate_ocean_scores(answers):
  """Calculates OCEAN scores based on provided answers.

  Args:
    answers: A dictionary of question-answer pairs.

  Returns:
    A Pandas DataFrame with factors and scores.
  """

  # Define reverse score questions for each factor
  reverse_questions = {
      'Extraversion': [2, 5, 7, 9],
      'Neuroticism': [11, 14, 16],
      'Openness': [18, 22, 24, 25],
      'Agreeableness': [26, 28, 31, 33],
      'Conscientiousness': [35, 37, 38, 41]
  }

  def calculate_factor_score(factor, answers):
    reverse_items = reverse_questions[factor]
    normal_items = [int(q) for q in answers.keys() if int(q) not in reverse_items]

    # Reverse score for reverse items
    for q in reverse_items:
      answers[str(q)] = 6 - answers[str(q)]

    # Calculate factor score
    factor_score = sum(answers[str(q)] for q in normal_items) / len(normal_items)
    return factor_score

  # Calculate scores for each factor
  ocean_scores = {}
  for factor in reverse_questions.keys():
    ocean_scores[factor] = calculate_factor_score(factor, answers)

  # Create DataFrame
  df = pd.DataFrame({'factors': list(ocean_scores.keys()), 'scores': list(ocean_scores.values())})
  return df

final = calculate_ocean_scores(all_answer)
final