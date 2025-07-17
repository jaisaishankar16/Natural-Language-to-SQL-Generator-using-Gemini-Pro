import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from constants import GOOGLE_API_KEY

## Configure our API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

##Function to load Google Gemini pro and provide sql as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-2.0-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function to retrieve query from SQL Database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


## Define prompt

prompt=[
      """
You are an expert in converting English questions to SQL query!
The SQL Database has the name STUDENT and has the following columns - NAME, CLASS,SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of
records are present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
\nExample 2 - Tell me all the students studying in Data Science class?,
the SQL command will be something like this SELECT * from STUDENT where CLASS="DATA SCIENCE";
also the sql code should not have ``` in beginning or end and sql word in the output
"""
]

## Streamlit App

st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question=st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

# if submit button is clicked

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)