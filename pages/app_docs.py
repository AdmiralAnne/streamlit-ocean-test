import streamlit as st
import pandas as pd

st.subheader("Run-through of how we build this app (It's preety simple, and straight forward 📏)")

st.info("I'll take you through the step-by-step process of how we built this app using Streamlit and Python.")

st.divider()

st.write("**Setting Up the Streamlit App**")
st.markdown("""
- Login to streamlit, create a new app and link it to your existing GitHub Repository.
- That's preety much it.
- Ah yes, dont't forget to install the dependencies from requirements.txt.
""")

st.divider()

st.write('**Importing the Dataset**')

st.text("""
We needed a set of predefined questions. 
We stored these questions in a CSV file named OCEAN_questions.csv. 
The dataset is then imported using Pandas' pd.read_csv() function, 
which reads the CSV file into a DataFrame.
""")
st.markdown(""" Source of questions can be found here:
[Online Library Wiley Pdf](https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781118638279.app1)
""")

code = '''
    try:
        data = pd.read_csv("OCEAN_questions.csv")
        questions = data.loc[:, ["ID", "question", "choice"]]
    except FileNotFoundError:
        st.error("Error: 'OCEAN_questions.csv' file not found. Please ensure the file exists in the same directory as your script.")
        exit()
    '''
st.code(code, language="python")

st.divider()

st.write('**Displaying the questions**')

st.write("""
**all_answers dictionary** : The user responses are stored in this dictionary, with the question ID as the key and the selected answer as the value. We Iterate through all the questions (row items) and print it, with 5 options.
""")

code1 = '''
    all_answers = {}
    for index, row in questions.iterrows():
        question_id = row['ID']
        question_text = row['question']
         = st.radio(f"Question {question_id}: **{question_text}**", options=[1, 2, 3, 4, 5],
                     captions=[
                         "Disagree strongly",
                         "Disagree a little",
                         "Neither agree nor disagree",
                         "Agree a little",
                         "Agree strongly"
                     ],
                     horizontal=False, key=question_id)
    all_answers[question_id] = answer
    '''
st.code(code1, language="python")

st.divider()

st.write('**Converting Responses to a DataFrame**')

st.write("""
Now we need to convert the dict from the above step, into a proper dataframe. This custom function **dict_to_dataframe()** takes a dictionary as input and converts it into a Pandas DataFrame, it's just easier to work with dfs.
""")

code2 = '''
    def dict_to_dataframe(data_dict):
    # Convert the dictionary to a list of tuples
    data = [(k, v) for k, v in data_dict.items()]
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=['ID', 'answer'])
    return df

    answers_df = dict_to_dataframe(all_answers)
    '''
st.code(code2, language="python")

st.divider()

st.write('**Scoring the OCEAN Traits**')

st.write("""
    All we did here was screate a function: **calculate_ocean_scores(df)** that calculates all the scores for each trait using the reference pdf, with normal score ids and reverse score ids. We have another smaller function to reverse the score if it matches the specified ids.
    Later we store it in a variable: ocean_scores(which is a dictionary with the final scores, we will also convert this to a dataframe.)
""")

code3 = '''
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
    '''
st.code(code3, language="python")

st.divider()

st.write('**Displaying the Results**')

st.write("""
    Simply display the new dataframe witht the final ocean test scores.
    And then, we created a rather long and.. tedious function that displays the appropriate interpretation of your test, according to the score you got. We just use Conditional if else statements for this.
""")

code4 = '''
    # Function to get the interpretation based on the score
    def get_interpretation(trait, score):
        if trait == "Openness":
            with st.expander("**Openness to Experience (O)**"):
                if 9 <= score <= 18:
                    st.write("Interpretation text here...")
                elif 19 <= score <= 27:
                    st.write("Interpretation text here...")
                elif 28 <= score <= 36:
                    st.write("Interpretation text here...")
                elif 37 <= score <= 45:
                    st.write("Interpretation text here...")
                st.write("Further Reading: https://bigfive-test.com/articles/openness")
        # Simply repeat this for other traits...
    '''
st.code(code4, language="python")

st.divider()

st.write("Tabbed Layout and Sidebar")

st.write("Create 2 tabs, one for the results table and another one for the interpretations.")

code5 = '''
    tab1, tab2 = st.tabs(["Score Table", "Insights"])

    with tab1:
        scores_df

    with tab2:
        for index, row in scores_df.iterrows():
            get_interpretation(row['Trait'], row['Score'])
        st.info("**Remember:** These are general guidelines and **individual differences** exist. Let this serve as a high level overview of    your traits, not a one stop solution.")

    with st.sidebar:
        st.success('Navigate to more pages using the above links ⬆️')
    '''
st.code(code5, language="python")

st.divider()

st.info("That's preety much it, it's a simple program wiht little to no complexity but the scores we attain from this test can further help us to create an even more comprehensive Interpretation - such as Personalized advice, Jobs Recommendation, Techniques to get better at certain traits if you wish etc. . .")

st.success("Ciao! Special thanks to the entire team who helped bring this project to life!")