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