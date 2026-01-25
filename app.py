from dotenv import load_dotenv
load_dotenv() ## load all the environment variables from the .env file

import streamlit as st
import google.generativeai as genai
import os
import sqlite3
import pandas as pd

## configure the api key for the google generative ai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Functio to google gemeni model and provide query as response
def get_gemini_response(question, promt):
    model = genai.GenerativeModel(model_name="gemini-3-flash-preview")
    response = model.generate_content([prompt[0], question])
    return response.text

## Function to retrieve query from the sql database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
    return df

prompt = ["""
You are a helpful assistant that can answer questions about the student database.
You can answer questions about the students, their classes, their sections, and their marks.
You can also answer questions about the students, their classes, their sections, and their marks.
For Example:How many students are in the database?
Answer: SELECT COUNT(*) FROM STUDENT;
For Example:What is the average marks of the students?
Answer: SELECT AVG(MARKS) FROM STUDENT;
For Example:What is the total marks of the students?
Answer: SELECT SUM(MARKS) FROM STUDENT;
For Example:What is the maximum marks of the students?
Answer: SELECT MAX(MARKS) FROM STUDENT;
For Example:What is the minimum marks of the students?
Answer: SELECT MIN(MARKS) FROM STUDENT;
For Example:What is the students with the highest marks?
Answer: SELECT * FROM STUDENT ORDER BY MARKS DESC LIMIT 1;
Also sql code should not have ''' ''' in the answer.
"""]

## Streamlit app
st.set_page_config(page_title="I can retrieve any sql query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The response is:")
    st.dataframe(data)
