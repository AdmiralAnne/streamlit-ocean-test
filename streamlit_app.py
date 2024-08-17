import streamlit as st
import pandas as pd
from fpdf import FPDF

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
    * **Very High Score (16-21):** Highly imaginative and intellectually curious, with a strong preference for novelty and exploration. You're likely to be adventurous and open-minded in your approach to life.
    * **High Score (12-15):** Demonstrates a willingness to engage with new ideas and experiences. You are likely curious and flexible in your thinking.
    * **Average Score (-3-11):** Maintains a balance between openness and a preference for routine. You are likely to be adaptable but also value stability.
    * **Moderately Low Score (-8-2):** Prefers familiar environments and routines. You may be seen as practical and conservative in your outlook.
    * **Very Low Score (-15 to -7):** Highly conventional and resistant to change. You may be seen as closed-minded and traditional.

* **Conscientiousness:**  
    * **Very High Score (16-21):** Exceptionally organized and disciplined, with a strong sense of responsibility and goal-orientation. You likely exhibit perfectionism and a strong work ethic.
    * **Moderately High Score (12-15):** Demonstrates a good level of organization and time management. You are likely reliable and dependable.
    * **Average Score (-3-11):** Balances structure with flexibility. You may be adaptable but also capable of meeting deadlines.
    * **Moderately Low Score (-8-2):** Tends to be impulsive and disorganized. You may struggle with time management and meeting commitments.
    * **Very Low Score (-15 to -7):** Highly spontaneous and careless. You may have difficulty with planning and adhering to routines.            

* **Extraversion:**  
    * **Very High Score (16-21):** Extremely outgoing and energetic. You thrive in social settings and enjoy being the center of attention. You are likely assertive and enthusiastic.
    * **Moderately High Score (12-15):** Sociable and confident. You enjoy social interactions but also value alone time. You are likely to be assertive and expressive.
    * **Average Score (-3-11):** Balanced between introversion and extraversion. You can adapt to social situations but also enjoy solitude. You are likely to be versatile in social settings.
    * **Moderately Low Score (-8-2):** Prefers solitary activities and quiet environments. You may be seen as reserved or introverted.
    * **Very Low Score (-15 to -7):** Highly introverted and avoids social situations. You may be perceived as shy or reclusive

* **Agreeableness:**  
    * **Very High Score (16-21):** Extremely cooperative and empathetic. You prioritize others' needs and value harmony. You are likely trusting and forgiving.
    * **Moderately High Score (12-15):** Generally cooperative and considerate. You are likely to be helpful and supportive of others.
    * **Average Score (-3-11):** Balances cooperation with assertiveness. You can be both cooperative and competitive depending on the situation.
    * **Moderately Low Score (-8-2):** Can be assertive and competitive. You may be less concerned with others' feelings and more focused on personal goals.
    * **Very Low Score (-15 to -7):** Highly suspicious and distrustful. You may be seen as hostile or manipulative.  

* **Neuroticism:**  
    * **Very High Score(16-21):** Highly prone to anxiety, mood swings, worry, and emotional instability. May struggle to cope with stress.
    * **Moderately High Score(12-15):** Experiences moderate levels of anxiety and stress. May be easily frustrated or emotional.
    * **Average Score (3-11):** Generally experiences emotional stability but may face occasional stress or worry.
    * **Moderately Low Score(-8-2):** Generally calm and resilient. May not experience anxiety or stress frequently.
    * **Very Low Score(-15 to -7):** Highly emotionally stable and relaxed. Rarely experiences anxiety or stress. (**Note:** Extremely low scores might indicate a lack of emotional awareness)

**Please remember:** These are general descriptions, and individual differences exist. Interpreting scores should consider the specific context and purpose of the assessment.

""")

with st.expander("Results Dataframe"):
    st.text("collection of your responses:")
    answers_df

text_contents = '''
"Extraversion": extraversion_score,
"Neuroticism": neuroticism_score,
"Openness": openness_score,
"Agreeableness": agreeableness_score,
"Conscientiousness": conscientiousness_score

General Interpretations for OCEAN Traits

* **Openness to Experience (Openness)**:  
    * **Very High Score (16-21):** Highly imaginative and intellectually curious, with a strong preference for novelty and exploration. You're likely to be adventurous and open-minded in your approach to life.
    * **High Score (12-15):** Demonstrates a willingness to engage with new ideas and experiences. You are likely curious and flexible in your thinking.
    * **Average Score (-3-11):** Maintains a balance between openness and a preference for routine. You are likely to be adaptable but also value stability.
    * **Moderately Low Score (-8-2):** Prefers familiar environments and routines. You may be seen as practical and conservative in your outlook.
    * **Very Low Score (-15 to -7):** Highly conventional and resistant to change. You may be seen as closed-minded and traditional.

* **Conscientiousness:**  
    * **Very High Score (16-21):** Exceptionally organized and disciplined, with a strong sense of responsibility and goal-orientation. You likely exhibit perfectionism and a strong work ethic.
    * **Moderately High Score (12-15):** Demonstrates a good level of organization and time management. You are likely reliable and dependable.
    * **Average Score (-3-11):** Balances structure with flexibility. You may be adaptable but also capable of meeting deadlines.
    * **Moderately Low Score (-8-2):** Tends to be impulsive and disorganized. You may struggle with time management and meeting commitments.
    * **Very Low Score (-15 to -7):** Highly spontaneous and careless. You may have difficulty with planning and adhering to routines.            

* **Extraversion:**  
    * **Very High Score (16-21):** Extremely outgoing and energetic. You thrive in social settings and enjoy being the center of attention. You are likely assertive and enthusiastic.
    * **Moderately High Score (12-15):** Sociable and confident. You enjoy social interactions but also value alone time. You are likely to be assertive and expressive.
    * **Average Score (-3-11):** Balanced between introversion and extraversion. You can adapt to social situations but also enjoy solitude. You are likely to be versatile in social settings.
    * **Moderately Low Score (-8-2):** Prefers solitary activities and quiet environments. You may be seen as reserved or introverted.
    * **Very Low Score (-15 to -7):** Highly introverted and avoids social situations. You may be perceived as shy or reclusive

* **Agreeableness:**  
    * **Very High Score (16-21):** Extremely cooperative and empathetic. You prioritize others' needs and value harmony. You are likely trusting and forgiving.
    * **Moderately High Score (12-15):** Generally cooperative and considerate. You are likely to be helpful and supportive of others.
    * **Average Score (-3-11):** Balances cooperation with assertiveness. You can be both cooperative and competitive depending on the situation.
    * **Moderately Low Score (-8-2):** Can be assertive and competitive. You may be less concerned with others' feelings and more focused on personal goals.
    * **Very Low Score (-15 to -7):** Highly suspicious and distrustful. You may be seen as hostile or manipulative.  

* **Neuroticism:**  
    * **Very High Score(16-21):** Highly prone to anxiety, mood swings, worry, and emotional instability. May struggle to cope with stress.
    * **Moderately High Score(12-15):** Experiences moderate levels of anxiety and stress. May be easily frustrated or emotional.
    * **Average Score (3-11):** Generally experiences emotional stability but may face occasional stress or worry.
    * **Moderately Low Score(-8-2):** Generally calm and resilient. May not experience anxiety or stress frequently.
    * **Very Low Score(-15 to -7):** Highly emotionally stable and relaxed. Rarely experiences anxiety or stress. (**Note:** Extremely low scores might indicate a lack of emotional awareness)

**Please remember:** These are general descriptions, and individual differences exist. Interpreting scores should consider the specific context and purpose of the assessment.

'''
st.download_button("Download some text", text_contents)