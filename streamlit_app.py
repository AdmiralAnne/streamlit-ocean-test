import streamlit as st
import pandas as pd

st.title('OCEAN Test App')

st.info("""
This test offers insights into your traits. Be honest!

* Answer statements using a 1-5 scale (1 = disagree strongly, 5 = agree strongly)
* There is no time limit, answer thoughtfully.

**Please answer all questions before submitting.**
""")

# Import the CSV dataset and read the file
try:
  data = pd.read_csv("OCEAN_questions.csv")
  questions = data.loc[:, ["ID", "question", "choice", "factor"]]
except FileNotFoundError:
  st.error("Error: 'OCEAN_questions.csv' file not found. Please ensure the file exists in the same directory as your script.")
  exit()

def calculate_ocean_scores(df):
  """Calculates OCEAN scores based on the provided DataFrame.

  Args:
    df: The DataFrame containing question data (ID, question, factor, choice).

  Returns:
    A dictionary containing the OCEAN scores.
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

    # Reverse score for reverse items (using choice column directly)
    df.loc[df['ID'].isin(reverse_items), 'choice'] = 6 - df['choice']

    # Calculate factor score (handle potential missing values)
    factor_score = df[df['factor'] == factor]['choice'].mean(skipna=True)
    score
    return factor_score

  # Calculate scores for each factor
  ocean_scores = {}
  for factor in ['Extraversion', 'Neuroticism', 'Openness', 'Agreeableness', 'Conscientiousness']:
    ocean_scores[factor] = calculate_factor_score(factor, df.copy())  # Avoid modifying original DataFrame

  return ocean_scores

# Display questions with radio buttons
all_answers = {}  # Not used for score calculation anymore

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

# No need to create a separate DataFrame from all_answers

# Calculate OCEAN scores directly using the 'choice' column in df
ocean_scores = calculate_ocean_scores(data)

# Display results
st.success("Thank you for completing the test!")
st.subheader("Your OCEAN Scores:")
for factor, score in ocean_scores.items():
  st.write(f"{factor}: {score:.2f}")