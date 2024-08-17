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

* **Openness to Experience (Openness)**:  
    * **Very High Score (16-21):** Highly curious, imaginative, and intellectually driven. Seeks new experiences and enjoys novelty. Appreciates art, philosophy, and creative endeavors.
    * **Moderately High Score (11-15):** Open to new ideas and experiences, but also values familiarity. Enjoys learning and exploring within their interests.
    * **Average Score (6-10):** Balanced between openness and preference for routine. May be open to new things in certain contexts.
    * **Moderately Low Score (1-5):** Prefers routine and familiar experiences. May be skeptical of new ideas or approaches.
    * **Very Low Score (-5 to 0):** Highly practical and conventional. May resist change and focus on established ways of doing things.

* **Conscientiousness:**  
    * **Very High Score (16-21):** Extremely organized, disciplined, reliable, and goal-oriented. Strives for perfection and maintains a strong work ethic.
    * **Moderately High Score (11-15):** Well-organized, responsible, and dependable. Manages time and resources effectively.
    * **Average Score (6-10):** Moderately organized and reliable, but may be flexible with details and deadlines.
    * **Moderately Low Score (1-5):** Can be disorganized and impulsive. May struggle with deadlines and task completion.
    * **Very Low Score (-5 to 0):** Highly spontaneous and carefree. May show disregard for rules and planning.

* **Extraversion:**  
    * **Very High Score (16-21):** Highly outgoing, social, and energetic. Craves stimulation and enjoys being the center of attention. Thrives in social settings.
    * **Moderately High Score (11-15):** Enjoys social interaction but also values time alone. Comfortable in social situations and assertive in expressing themselves.
    * **Average Score (6-10):** Balanced between introversion and extraversion. Can enjoy social interaction but also needs time to recharge alone.
    * **Moderately Low Score (1-5):** Prefers solitude and quiet environments. May feel drained by prolonged social interaction.
    * **Very Low Score (-5 to 0):** Highly introverted and reserved. Avoids large groups or social gatherings.

* **Agreeableness:**  
    * **Very High Score (16-21):** Extremely cooperative, trusting, compassionate, and puts others' needs first. Values harmony and avoids conflict.
    * **Moderately High Score (11-15):** Generally cooperative and helpful. Considers others' perspectives and prioritizes maintaining positive relationships.
    * **Average Score (6-10):** Balanced between cooperation and assertiveness. Can express needs while being considerate of others.
    * **Moderately Low Score (1-5):** Can be competitive and assertive. May prioritize personal goals over others' needs.
    * **Very Low Score (-5 to 0):** Highly suspicious and distrustful. May be seen as self-centered and prioritize personal gain over cooperation.

* **Neuroticism:**  
    * **Very High Score (16-21):** Highly prone to anxiety, mood swings, worry, and emotional instability. May struggle to cope with stress.
    * **Moderately High Score (11-15):** Experiences moderate levels of anxiety and stress. May be easily frustrated or emotional.
    * **Average Score (6-10):** Generally experiences emotional stability but may face occasional stress or worry.
    * **Moderately Low Score (1-5):** Generally calm and resilient. May not experience anxiety or stress frequently.
    * **Very Low Score (-5 to 0):** Highly emotionally stable and relaxed. Rarely experiences anxiety or stress. (**Note:** Extremely low scores might indicate a lack of emotional awareness)

**Please remember:** These are general descriptions, and individual differences exist. Interpreting scores should consider the specific context and purpose of the assessment.

""")