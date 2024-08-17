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
scores_df = dict_to_dataframe(ocean_scores)
new_columns = ['Trait', 'Score ']
scores_df.columns = new_columns
scores_df


st.info(""" 
**General Interpretaion of scores**
""")

with st.expander("**Openness to Experience (O)**"):
    st.write("""
    
    **Very Low (9-18):** Individuals in this range tend to be more traditional, practical, and down-to-earth. They may be less interested in new ideas or experiences and prefer familiar routines.
    
    **Low (19-27):** Somewhat conventional, but open to new experiences within their comfort zone. They might be cautious about trying new things but adaptable to change.

    **Average (28-36):** Balanced approach to new experiences. They are open to learning and trying new things but also appreciate routine and stability.

    **High (37-45):** Highly imaginative and curious individuals. They are open to new ideas and experiences, often seeking out intellectual stimulation and artistic pursuits.
    """)

with st.expander("**Conscientiousness (C)**"):
    st.write("""  
    **Very Low (9-18):** Individuals in this range may be more spontaneous, impulsive, and less focused on goals. They may struggle with organization and time management.

    **Low (19-27):** Relatively laid-back and easygoing, but can be inconsistent in their approach to tasks and responsibilities.

    **Average (28-36):** Generally organized and reliable, able to balance spontaneity with responsibility.

    **High (37-45):** Highly organized, disciplined, and goal-oriented individuals. They are likely to be dependable and hardworking.
    """)

with st.expander("**Extraversion (E)**"):
    st.write("""  
    **Very Low (9-18):** Individuals in this range tend to be introverted, preferring solitary activities or small groups. They may be seen as reserved or shy.

    **Low (19-27):** Moderate level of extraversion, enjoying social interaction but also valuing alone time. They may be seen as balanced or ambiverted.

    **Average (28-36):** Outgoing and sociable individuals who enjoy being around people. They are likely to be assertive and enthusiastic.

    **High (37-45):** Extremely extraverted, with a strong desire for social interaction and stimulation. They are often seen as energetic and charismatic.
    """)

with st.expander("**Agreeableness (A)**"):
    st.write("""  
    **Very Low (9-18):** Individuals in this range tend to be assertive, competitive, and focused on their own needs. They may be seen as skeptical or distrustful.

    **Low (19-27):** Somewhat assertive and independent, but also able to cooperate with others. They might be seen as balanced in their approach to social interactions.

    **Average (28-36):** Cooperative and considerate, valuing harmony in relationships. They are likely to be helpful and empathetic.

    **High (37-45):** Extremely altruistic and empathetic, often prioritizing the needs of others over their own. They may be seen as overly accommodating.
    """)

with st.expander("**Neuroticism (N)**"):
    st.write("""  
    **Very Low (9-18):** Emotionally stable and resilient, able to handle stress effectively. They may be seen as calm and collected.

    **Low (19-27):** Generally emotionally stable, but may experience occasional mood swings or anxiety.

    **Average (28-36):** Prone to moderate levels of anxiety and emotional reactivity. They may experience stress and worry more frequently.

    **High (37-45):** High levels of neuroticism, characterized by anxiety, mood swings, and difficulty coping with stress.    
    """)

st.info("**Remember: These descriptions provide general guidelines and individual differences exist. It's essential to consider the specific context and purpose of the assessment when interpreting scores.**")

with st.expander("Results Dataframe"):
    st.text("Dataset and collections of your responses:")
    data
    answers_df
    ocean_scores

for trait, score in ocean_scores.items():
    with st.expander(trait):
        if score >= 9 and score <= 18:
            st.info(f"**Very Low ({score}):**\n"
                   "* You are likely to value tradition and practicality, often finding comfort in the familiar and routine. This preference might make you less inclined to seek out novel experiences or ideas, which can be beneficial in environments that require consistency and reliability. However, it may also limit your exposure to diverse perspectives and innovative solutions. Consider gradually introducing new experiences into your life to enhance creativity and adaptability.")
        elif score >= 19 and score <= 27:
            st.info(f"**Low ({score}):**\n"
                   "* While you may lean towards conventionality, you are open to exploring new experiences within your comfort zone. This cautious approach allows you to adapt to change without feeling overwhelmed. You might benefit from occasionally stepping outside your comfort zone to foster personal growth and broaden your horizons, which can lead to unexpected opportunities and insights.")
        elif score >= 28 and score <= 36:
            st.info(f"**Average ({score}):**\n"
                   "* You strike a balance between embracing new experiences and valuing routine. This equilibrium allows you to enjoy the stability of familiar patterns while remaining open to learning and growth. You are likely to appreciate both intellectual stimulation and the comfort of routine, making you adaptable in various situations. Consider leveraging this balance to explore new interests while maintaining a sense of stability.")
        else:
            st.info(f"**High ({score}):**\n"
                   "* Your high level of openness suggests a strong curiosity and imagination, often driving you to seek out intellectual and artistic pursuits. You thrive on new ideas and experiences, which can lead to innovative thinking and creative problem-solving. While this trait can be a significant asset, be mindful of the potential for becoming easily bored with routine tasks. Channel your curiosity into projects that challenge and inspire you.")

    with st.expander("Conscientiousness (C)"):
        if score >= 9 and score <= 18:
            st.info(f"**Very Low ({score}):**\n"
                   "* You may find yourself acting spontaneously and impulsively, often prioritizing immediate gratification over long-term goals. This can lead to challenges with organization and time management, potentially impacting your ability to meet responsibilities. Consider developing strategies to enhance your focus and discipline, such as setting clear goals and creating structured routines to improve productivity and reliability.")
        elif score >= 19 and score <= 27:
            st.info(f"**Low ({score}):**\n"
                   "* Your laid-back and easygoing nature allows you to adapt to changing circumstances, but it may also result in inconsistency in task completion. While this flexibility can be advantageous in dynamic environments, it might hinder your ability to achieve long-term objectives. Strive to find a balance between spontaneity and responsibility by setting achievable goals and maintaining a flexible yet structured approach to tasks.")
        elif score >= 28 and score <= 36:
            st.info(f"**Average ({score}):**\n"
                   "* You exhibit a balanced approach to conscientiousness, effectively managing responsibilities while allowing room for spontaneity. This makes you reliable and adaptable, capable of handling both planned and unexpected situations. Use this balance to your advantage by setting realistic goals and maintaining a flexible mindset, which can enhance your ability to navigate various challenges.")
        else:
            st.info(f"**High ({score}):**\n"
                   "* Your high conscientiousness indicates a strong sense of discipline and organization, often making you dependable and goal-oriented. You likely excel in structured environments where attention to detail and perseverance are valued. While this trait is beneficial for achieving success, be cautious of becoming overly rigid or perfectionistic. Allow yourself moments of spontaneity to foster creativity and prevent burnout.")