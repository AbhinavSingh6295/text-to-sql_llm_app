from dotenv import load_dotenv
load_dotenv() ## load all the environment variables from the .env file

import streamlit as st
import google.generativeai as genai
import os
import sqlite3
import pandas as pd
from db_connection import DatabaseConnection

## configure the api key for the google generative ai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Functio to google gemeni model and provide query as response
def get_gemini_response(question, promt, schema_info, db_type):
    model = genai.GenerativeModel(model_name="gemini-3-flash-preview")
    full_prompt = prompt[0]
    if schema_info:
        full_prompt += f"\n\nDatabase Schema:\n{schema_info}"
     # Add PostgreSQL-specific instruction
    if db_type == "postgresql":
        full_prompt += "\n\nIMPORTANT: For PostgreSQL databases, you MUST use the full table name format: schema_name.table_name in all SQL queries. For example, use 'legacy_dm.fact_live_product_sales' instead of just 'fact_live_product_sales'."
    response = model.generate_content([full_prompt, question])
    return response.text

## Function to retrieve query from the sql database
def read_sql_query(sql, db_conn):
    df = db_conn.execute_query(sql)
    db_conn.close()
    return df

prompt = ["""
You are a helpful assistant that can answer questions about the student database.
You can answer questions about the students, their classes, their sections, and their marks.
You can also answer questions about the students, their classes, their sections, and their marks.
Please don't include the keyword 'Answer:' in the response.
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

base_prompt = ["""
You are an expert SQL query generator. Your task is to convert natural language questions into accurate SQL queries.

IMPORTANT RULES:
1. Generate ONLY the SQL query, nothing else
2. Do NOT include markdown code blocks (no ```sql or ```)
3. Do NOT include any explanatory text before or after the query
4. Use proper SQL syntax for the database type
5. Be precise with table and column names (respect case sensitivity)
6. Use appropriate SQL functions (COUNT, SUM, AVG, MAX, MIN, etc.) when needed
7. Include proper WHERE clauses for filtering
8. Use JOINs when querying multiple tables
9. Use LIMIT for top N queries when appropriate
10. Please avoid adding the keyword 'Answer:' in the response.
12. For PostgreSQL databases: ALWAYS use schema.table_name format (e.g., legacy_dm.fact_live_product_sales)

Examples:
Question: How many records are in the users table?
Answer: SELECT COUNT(*) FROM users;

Question: What is the average salary of employees?
Answer: SELECT AVG(salary) FROM employees;

Question: Show me the top 10 customers by revenue
Answer: SELECT * FROM customers ORDER BY revenue DESC LIMIT 10;

Question: Find all orders placed in 2024
Answer: SELECT * FROM orders WHERE YEAR(order_date) = 2024;

Remember: Return ONLY the SQL query, no explanations, no markdown formatting.
"""]

## Streamlit app
st.set_page_config(page_title="I can retrieve any sql query", page_icon=":database:", layout="wide")
st.header("Text to SQL Query Generator")
st.markdown("Ask questions in natural language and get SQL queries generated and executed.")

with st.sidebar:
    st.subheader("Database Configuration")
    DB_TYPE = st.selectbox(
        "Select Database Type",
        options=["sqllite", "postgresql"],
        index=0,
        help="Select the database type to connect to",
        key="db_type_selector"
    )
    st.markdown(f"**Database Type**: {DB_TYPE}")

db_connection = DatabaseConnection(db_type=DB_TYPE)
db_connection.connect()
schema_info = db_connection.get_schema_info()
st.sidebar.success("Connected to the database")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt+base_prompt, schema_info, DB_TYPE)
    print(response)
    data = read_sql_query(response, db_connection)
    st.subheader("The response is:")
    st.dataframe(data)

# Footer
st.markdown("---")
st.markdown("💡 **Tip:** Be specific in your questions for better SQL generation. Include table names, column names, and filtering criteria when possible.")
