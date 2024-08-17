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

# questions
# data
# all_answers

def dict_to_dataframe(data_dict):
  # Convert the dictionary to a list of tuples
  data = [(k, v) for k, v in data_dict.items()]
  # Create a DataFrame from the list of tuples
  df = pd.DataFrame(data, columns=['ID', 'answer'])
  return df


answers_df = dict_to_dataframe(all_answers)

# Define reverse score questions for each factor
reverse_questions = {
    'Extraversion': [2, 5, 7, 9],
    'Neuroticism': [11, 14, 16],
    'Openness': [18, 22, 24, 25],
    'Agreeableness': [26, 28, 31, 33],
    'Conscientiousness': [35, 37, 38, 41]
}

# Function to reverse score values
def reverse_score(value):
    return 6 - value

# Manual calculations for OCEAN scores
def calculate_ocean_scores(df):
    extraversion_score = (df[df['ID'].isin([1, 3, 4, 6, 8])]['answer'].sum() +
                          df[df['ID'].isin([2, 5, 7, 9])]['answer'].apply(reverse_score).sum())

    neuroticism_score = (df[df['ID'].isin([10, 12, 13, 15, 17])]['answer'].sum() +
                           df[df['ID'].isin([11, 14, 16])]['answer'].apply(reverse_score).sum())

    openness_score = (df[df['ID'].isin([19, 20, 21, 23])]['answer'].sum() +
                       df[df['ID'].isin([18, 22, 24, 25])]['answer'].apply(reverse_score).sum())

    agreeableness_score = (df[df['ID'].isin([27, 29, 30, 32])]['answer'].sum() +
                           df[df['ID'].isin([26, 28, 31, 33])]['answer'].apply(reverse_score).sum())

    conscientiousness_score = (df[df['ID'].isin([34, 36, 39, 40])]['answer'].sum() +
                               df[df['ID'].isin([35, 37, 38, 41])]['answer'].apply(reverse_score).sum())
                              
    print({'Extraversion': extraversion_score,
            'Neuroticism': neuroticism_score,
            'Openness': openness_score,
            'Agreeableness': agreeableness_score,
            'Conscientiousness': conscientiousness_score})

    return {'Extraversion': extraversion_score,
            'Neuroticism': neuroticism_score,
            'Openness': openness_score,
            'Agreeableness': agreeableness_score,
            'Conscientiousness': conscientiousness_score}

ocean_scores = calculate_ocean_scores(answers_df)
ocean_scores
scores_df = dict_to_dataframe(ocean_scores)
new_columns = ['Trait', 'Score']
scores_df.columns = new_columns
scores_df


st.info(""" 

Some text coming here later

""")

with st.expander("Results Dataframe"):
    st.text("collection of your responses:")
    data
    answers_df