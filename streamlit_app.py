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

    return {
            'Openness': openness_score,
            'Conscientiousness': conscientiousness_score,
            'Extraversion': extraversion_score,
            'Agreeableness': agreeableness_score,
            'Neuroticism': neuroticism_score
            }

ocean_scores = calculate_ocean_scores(answers_df)
scores_df = dict_to_dataframe(ocean_scores)
new_columns = ['Trait', 'Score ']
scores_df.columns = new_columns
scores_df

with st.expander("**Openness to Experience (O)**"):
    st.write("""
    **Very Low (9-18):** You are likely to value tradition and practicality, often finding comfort in the familiar and routine. This preference might make you less inclined to seek out novel experiences or ideas, which can be beneficial in environments that require consistency and reliability. However, it may also limit your exposure to diverse perspectives and innovative solutions. Consider gradually introducing new experiences into your life to enhance creativity and adaptability.

    **Low (19-27):** While you may lean towards conventionality, you are open to exploring new experiences within your comfort zone. This cautious approach allows you to adapt to change without feeling overwhelmed. You might benefit from occasionally stepping outside your comfort zone to foster personal growth and broaden your horizons, which can lead to unexpected opportunities and insights.

    **Average (28-36):** You strike a balance between embracing new experiences and valuing routine. This equilibrium allows you to enjoy the stability of familiar patterns while remaining open to learning and growth. You are likely to appreciate both intellectual stimulation and the comfort of routine, making you adaptable in various situations. Consider leveraging this balance to explore new interests while maintaining a sense of stability.

    **High (37-45):** Your high level of openness suggests a strong curiosity and imagination, often driving you to seek out intellectual and artistic pursuits. You thrive on new ideas and experiences, which can lead to innovative thinking and creative problem-solving. While this trait can be a significant asset, be mindful of the potential for becoming easily bored with routine tasks. Channel your curiosity into projects that challenge and inspire you.
    """)

with st.expander("**Conscientiousness (C)**"):
    st.write("""  
    **Very Low (9-18):** You may find yourself acting spontaneously and impulsively, often prioritizing immediate gratification over long-term goals. This can lead to challenges with organization and time management, potentially impacting your ability to meet responsibilities. Consider developing strategies to enhance your focus and discipline, such as setting clear goals and creating structured routines to improve productivity and reliability.

    **Low (19-27):** Your laid-back and easygoing nature allows you to adapt to changing circumstances, but it may also result in inconsistency in task completion. While this flexibility can be advantageous in dynamic environments, it might hinder your ability to achieve long-term objectives. Strive to find a balance between spontaneity and responsibility by setting achievable goals and maintaining a flexible yet structured approach to tasks.

    **Average (28-36):** You exhibit a balanced approach to conscientiousness, effectively managing responsibilities while allowing room for spontaneity. This makes you reliable and adaptable, capable of handling both planned and unexpected situations. Use this balance to your advantage by setting realistic goals and maintaining a flexible mindset, which can enhance your ability to navigate various challenges.

    **High (37-45):** Your high conscientiousness indicates a strong sense of discipline and organization, often making you dependable and goal-oriented. You likely excel in structured environments where attention to detail and perseverance are valued. While this trait is beneficial for achieving success, be cautious of becoming overly rigid or perfectionistic. Allow yourself moments of spontaneity to foster creativity and prevent burnout.
    """)

with st.expander("**Extraversion (E)**"):
    st.write("""  
    **Very Low (9-18):** You may prefer solitary activities or small, intimate gatherings, often finding energy in introspection and reflection. Others might perceive you as reserved or shy, but this introspective nature can lead to deep personal insights and meaningful connections with a select few. Embrace your introversion by seeking environments that allow for quiet reflection and personal growth, while also challenging yourself to engage in social interactions that align with your interests.

    **Low (19-27):** You enjoy social interactions but also value your alone time, often finding a balance between the two. This ambiverted nature allows you to adapt to various social settings, making you approachable yet independent. Use this balance to cultivate meaningful relationships while ensuring you have time for self-reflection and personal development.

    **Average (28-36):** You are likely outgoing and sociable, enjoying the company of others and thriving in social settings. Your assertiveness and enthusiasm make you a natural leader and communicator. Leverage these traits to build strong social networks and pursue opportunities that require collaboration and teamwork, while also ensuring you take time for self-care and introspection.

    **High (37-45):** Your strong desire for social interaction and stimulation often makes you energetic and charismatic. You likely excel in environments that require teamwork and communication, drawing energy from engaging with others. While your extraversion is a significant asset, be mindful of the need for occasional solitude to recharge and reflect. Balance your social activities with moments of introspection to maintain overall well-being.
    """)

with st.expander("**Agreeableness (A)**"):
    st.write("""  
    **Very Low (9-18):** You may prioritize your own needs and goals, often displaying assertiveness and competitiveness. Others might perceive you as skeptical or distrustful, but this focus on self-interest can drive personal achievement and resilience. Consider cultivating empathy and cooperation to enhance your interpersonal relationships and create a more harmonious social environment.

    **Low (19-27):** You exhibit a balance between assertiveness and cooperation, allowing you to maintain independence while working effectively with others. This balanced approach can lead to successful collaborations and personal growth. Use your assertiveness to advocate for yourself while remaining open to others' perspectives, fostering mutual respect and understanding.

    **Average (28-36):** You are likely cooperative and considerate, valuing harmony and empathy in your relationships. This makes you a supportive and understanding friend or colleague, often prioritizing the well-being of others. Leverage these traits to build strong, trusting relationships, while also ensuring you set boundaries to protect your own needs and interests.

    **High (37-45):** Your high agreeableness suggests a strong sense of altruism and empathy, often leading you to prioritize others' needs over your own. While this trait fosters deep connections and trust, be cautious of becoming overly accommodating or neglecting your own well-being. Strive to balance your empathy with self-care and assertiveness to maintain healthy relationships and personal fulfillment.
    """)

with st.expander("**Neuroticism (N)**"):
    st.write("""  
    **Very Low (9-18):** You are likely emotionally stable and resilient, often handling stress with calmness and composure. Others may see you as a source of stability and support, which can enhance your personal and professional relationships. Use your emotional resilience to navigate challenges effectively, while also remaining open to exploring and expressing your emotions to foster deeper self-awareness.

    **Low (19-27):** Generally emotionally stable, you may experience occasional mood swings or anxiety, but these are typically manageable. Your ability to maintain composure in stressful situations makes you a reliable and supportive presence for others. Continue to develop coping strategies to manage stress and maintain emotional balance, enhancing your overall well-being.

    **Average (28-36):** You may experience moderate levels of anxiety and emotional reactivity, often feeling stress and worry more frequently. This sensitivity can lead to heightened empathy and awareness of others' emotions, but it may also impact your own well-being. Focus on developing healthy coping mechanisms and self-care practices to manage stress and maintain emotional balance.

    **High (37-45):** Your high levels of neuroticism may manifest as anxiety, mood swings, and difficulty coping with stress. While this emotional sensitivity can enhance your empathy and creativity, it may also lead to challenges in maintaining emotional stability. Consider seeking support from mental health professionals or developing mindfulness practices to enhance your emotional resilience and well-being.
    """)
    
st.info("**Remember:** These descriptions provide general guidelines and individual differences exist. It's essential to consider the specific context and purpose of the assessment when interpreting scores.")

with st.expander("Results Dataframe"):
    st.text("Dataset and collections of your responses:")
    data
    answers_df
    ocean_scores

# adding new lines of code here:





# Function to get the interpretation based on the score
def get_interpretation(trait, score):
    if trait == "Openness":
        with st.expander("**Openness to Experience (O)**"):
            if 9 <= score <= 18:
                st.write("""
                **Very Low (9-18):** You are likely to value tradition and practicality, often finding comfort in the familiar and routine. This preference might make you less inclined to seek out novel experiences or ideas, which can be beneficial in environments that require consistency and reliability. However, it may also limit your exposure to diverse perspectives and innovative solutions. Consider gradually introducing new experiences into your life to enhance creativity and adaptability.
                """)
            elif 19 <= score <= 27:
                st.write("""
                **Low (19-27):** While you may lean towards conventionality, you are open to exploring new experiences within your comfort zone. This cautious approach allows you to adapt to change without feeling overwhelmed. You might benefit from occasionally stepping outside your comfort zone to foster personal growth and broaden your horizons, which can lead to unexpected opportunities and insights.
                """)
            elif 28 <= score <= 36:
                st.write("""
                **Average (28-36):** You strike a balance between embracing new experiences and valuing routine. This equilibrium allows you to enjoy the stability of familiar patterns while remaining open to learning and growth. You are likely to appreciate both intellectual stimulation and the comfort of routine, making you adaptable in various situations. Consider leveraging this balance to explore new interests while maintaining a sense of stability.
                """)
            elif 37 <= score <= 45:
                st.write("""
                **High (37-45):** Your high level of openness suggests a strong curiosity and imagination, often driving you to seek out intellectual and artistic pursuits. You thrive on new ideas and experiences, which can lead to innovative thinking and creative problem-solving. While this trait can be a significant asset, be mindful of the potential for becoming easily bored with routine tasks. Channel your curiosity into projects that challenge and inspire you.
                """)

    elif trait == "Conscientiousness":
        with st.expander("**Conscientiousness (C)**"):
            if 9 <= score <= 18:
                st.write("""
                **Very Low (9-18):** You may find yourself acting spontaneously and impulsively, often prioritizing immediate gratification over long-term goals. This can lead to challenges with organization and time management, potentially impacting your ability to meet responsibilities. Consider developing strategies to enhance your focus and discipline, such as setting clear goals and creating structured routines to improve productivity and reliability.
                """)
            elif 19 <= score <= 27:
                st.write("""
                **Low (19-27):** Your laid-back and easygoing nature allows you to adapt to changing circumstances, but it may also result in inconsistency in task completion. While this flexibility can be advantageous in dynamic environments, it might hinder your ability to achieve long-term objectives. Strive to find a balance between spontaneity and responsibility by setting achievable goals and maintaining a flexible yet structured approach to tasks.
                """)
            elif 28 <= score <= 36:
                st.write("""
                **Average (28-36):** You exhibit a balanced approach to conscientiousness, effectively managing responsibilities while allowing room for spontaneity. This makes you reliable and adaptable, capable of handling both planned and unexpected situations. Use this balance to your advantage by setting realistic goals and maintaining a flexible mindset, which can enhance your ability to navigate various challenges.
                """)
            elif 37 <= score <= 45:
                st.write("""
                **High (37-45):** Your high conscientiousness indicates a strong sense of discipline and organization, often making you dependable and goal-oriented. You likely excel in structured environments where attention to detail and perseverance are valued. While this trait is beneficial for achieving success, be cautious of becoming overly rigid or perfectionistic. Allow yourself moments of spontaneity to foster creativity and prevent burnout.
                """)

    elif trait == "Extraversion":
        with st.expander("**Extraversion (E)**"):
            if 9 <= score <= 18:
                st.write("""
                **Very Low (9-18):** You may prefer solitary activities or small, intimate gatherings, often finding energy in introspection and reflection. Others might perceive you as reserved or shy, but this introspective nature can lead to deep personal insights and meaningful connections with a select few. Embrace your introversion by seeking environments that allow for quiet reflection and personal growth, while also challenging yourself to engage in social interactions that align with your interests.
                """)
            elif 19 <= score <= 27:
                st.write("""
                **Low (19-27):** You enjoy social interactions but also value your alone time, often finding a balance between the two. This ambiverted nature allows you to adapt to various social settings, making you approachable yet independent. Use this balance to cultivate meaningful relationships while ensuring you have time for self-reflection and personal development.
                """)
            elif 28 <= score <= 36:
                st.write("""
                **Average (28-36):** You are likely outgoing and sociable, enjoying the company of others and thriving in social settings. Your assertiveness and enthusiasm make you a natural leader and communicator. Leverage these traits to build strong social networks and pursue opportunities that require collaboration and teamwork, while also ensuring you take time for self-care and introspection.
                """)
            elif 37 <= score <= 45:
                st.write("""
                **High (37-45):** Your strong desire for social interaction and stimulation often makes you energetic and charismatic. You likely excel in environments that require teamwork and communication, drawing energy from engaging with others. While your extraversion is a significant asset, be mindful of the need for occasional solitude to recharge and reflect. Balance your social activities with moments of introspection to maintain overall well-being.
                """)

    elif trait == "Agreeableness":
        with st.expander("**Agreeableness (A)**"):
            if 9 <= score <= 18:
                st.write("""
                **Very Low (9-18):** You may prioritize your own needs and goals, often displaying assertiveness and competitiveness. Others might perceive you as skeptical or distrustful, but this focus on self-interest can drive personal achievement and resilience. Consider cultivating empathy and cooperation to enhance your interpersonal relationships and create a more harmonious social environment.
                """)
            elif 19 <= score <= 27:
                st.write("""
                **Low (19-27):** You exhibit a balance between assertiveness and cooperation, allowing you to maintain independence while working effectively with others. This balanced approach can lead to successful collaborations and personal growth. Use your assertiveness to advocate for yourself while remaining open to others' perspectives, fostering mutual respect and understanding.
                """)
            elif 28 <= score <= 36:
                st.write("""
                **Average (28-36):** You are likely cooperative and considerate, valuing harmony and empathy in your relationships. This makes you a supportive and understanding friend or colleague, often prioritizing the well-being of others. Leverage these traits to build strong, trusting relationships, while also ensuring you set boundaries to protect your own needs and interests.
                """)
            elif 37 <= score <= 45:
                st.write("""
                **High (37-45):** Your high agreeableness suggests a strong sense of altruism and empathy, often leading you to prioritize others' needs over your own. While this trait fosters deep connections and trust, be cautious of becoming overly accommodating or neglecting your own well-being. Strive to balance your empathy with self-care and assertiveness to maintain healthy relationships and personal fulfillment.
                """)

    elif trait == "Neuroticism":
        with st.expander("**Neuroticism (N)**"):
            if 9 <= score <= 18:
                st.write("""
                **Very Low (9-18):** You are likely emotionally stable and resilient, often handling stress with calmness and composure. Others may see you as a source of stability and support, which can enhance your personal and professional relationships. Use your emotional resilience to navigate challenges effectively, while also remaining open to exploring and expressing your emotions to foster deeper self-awareness.
                """)
            elif 19 <= score <= 27:
                st.write("""
                **Low (19-27):** Generally emotionally stable, you may experience occasional mood swings or anxiety, but these are typically manageable. Your ability to maintain composure in stressful situations makes you a reliable and supportive presence for others. Continue to develop coping strategies to manage stress and maintain emotional balance, enhancing your overall well-being.
                """)
            elif 28 <= score <= 36:
                st.write("""
                **Average (28-36):** You may experience moderate levels of anxiety and emotional reactivity, often feeling stress and worry more frequently. This sensitivity can lead to heightened empathy and awareness of others' emotions, but it may also impact your own well-being. Focus on developing healthy coping mechanisms and self-care practices to manage stress and maintain emotional balance.
                """)
            elif 37 <= score <= 45:
                st.write("""
                **High (37-45):** Your high levels of neuroticism may manifest as anxiety, mood swings, and difficulty coping with stress. While this emotional sensitivity can enhance your empathy and creativity, it may also lead to challenges in maintaining emotional stability. Consider seeking support from mental health professionals or developing mindfulness practices to enhance your emotional resilience and well-being.
                """)

# Iterate through each row in the DataFrame and display the interpretation
for index, row in scores_df.iterrows():
    get_interpretation(row['Trait'], row['Score'])
