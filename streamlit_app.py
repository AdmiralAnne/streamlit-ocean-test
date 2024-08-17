import streamlit as st
import pandas as pd
st.title('OCEAN Test App')

st.info('A minimal way to take the OCEAN Test and get insights into your personality!')
df=pd.read_csv("OCEAN_questions - give me the sheet here as a table.csv")
df.rename(columns={'score': 'choice'})
df

import streamlit as st
import pandas as pd

def create_questionnaire(df):
    for index, row in df.iterrows():
        question = row['question']
        st.subheader(f"Question {index+1}: {question}")
        choice = st.radio(
            "Choose your answer:",
            options=[
                "1. Disagree strongly",
                "2. Disagree a little",
                "3. Neither agree nor disagree",
                "4. Agree a little",
                "5. Agree strongly"
            ]
        )
        df.loc[index, 'choice'] = int(choice[0])  # Extract the number from the choice string

    return df

def main():
    # Assuming your DataFrame is named 'df' and has 'question' and 'choice' columns
    df = pd.read_csv("your_data.csv")  # Replace with your data source

    df = create_questionnaire(df)

    # Do something with the completed DataFrame, e.g., save it
    df.to_csv("completed_questionnaire.csv", index=False)

if __name__ == "__main__":
    main()