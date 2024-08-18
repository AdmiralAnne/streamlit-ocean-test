import streamlit as st
import pandas as pd

st.subheader("Run-through of how we build this app (It's preety simple, and straight forward 📏)")

st.info("I'll take you through the step-by-step process of how we built this app using Streamlit and Python.")

st.divider()

st.subheader("Setting Up the Streamlit App")
st.markdown("""

1.Login to streamlit, create a new app and link it to your existing GitHub Repository.
2.That's preety much it.
3.Ah yes, dont't forget to install the dependencies from requirements.txt.

""")

st.divider()

st.write('Importing the Dataset')

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