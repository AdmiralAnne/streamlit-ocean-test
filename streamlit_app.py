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
  questions = data.loc[:, ["ID", "question", "choice"]]  # Assuming 'choice' column exists
except FileNotFoundError:
  st.error("Error: 'OCEAN_questions.csv' file not found. Please ensure the file exists in the same directory as your script.")
  exit()

# Create an empty DataFrame to store answers (use reset_index later)
answers_df = pd.DataFrame(columns=['ID', 'answer'])

# Display questions with radio buttons
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

  # Add answer and ID to the DataFrame (create a dictionary first)
  new_row = {'ID': question_id, 'answer': answer}
  answers_df = answers_df.append(new_row, ignore_index=True)

# Reset index to create a numeric index for the DataFrame
answers_df = answers_df.reset_index(drop=True)  # Drop the old (non-numeric) index

# Rest of your code for calculating OCEAN scores using answers_df...

# Display results (assuming you have functions for score calculation)
st.success("Thank you for completing the test!")
st.subheader("Your OCEAN Scores:")
extraversion_score = calculate_ocean_scores(answers_df)["Extraversion"]  # Assuming a function
# ... calculate and display other scores similarly
st.write("Extraversion:", extraversion_score)
st.write("Neuroticism:", calculate_ocean_scores(answers_df)["Neuroticism"])
# ... display other scores