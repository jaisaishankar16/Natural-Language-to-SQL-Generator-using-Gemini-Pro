# **Gemini App to Retrieve SQL Data**
## Problem Statement
Solves the problem of converting English questions to SQL queries and retrieving data from a SQLite database.

## Dependencies and Requirements
* Python 3.8 or higher
* `streamlit` library for building the web app
* `google.generativeai` library for generating responses
* `sqlite3` library for interacting with the SQLite database
* `constants` file with `GOOGLE_API_KEY` variable
* `sql` file with SQLite database connection and table creation

## Project Structure
The project consists of two main files:
* `app.py`: The main application file that sets up the Streamlit app and defines the functions for generating responses and retrieving data.
* `constants.py`: A file that contains the `GOOGLE_API_KEY` variable.
* `sql.py`: A file that contains the SQLite database connection and table creation code.

## How to Run
1. Install the required libraries by running `pip install streamlit google.generativeai sqlite3`.
2. Set the `GOOGLE_API_KEY` variable in the `constants.py` file.
3. Run the `app.py` file using `streamlit run app.py`.
4. Open the app in your web browser by navigating to `http://localhost:8501`.
5. Input your question in the text input field and click the "Ask the question" button.
6. The app will generate a response and retrieve the corresponding data from the SQLite database.
7. The retrieved data will be displayed in the app.

## Ideology and Solution
The app uses the `google.generativeai` library to generate responses to the user's questions. It defines a function `get_gemini_response` that takes a question and a prompt as input and generates a response. The response is then used to retrieve data from the SQLite database using the `read_sql_query` function.

## Technologies Used
* `streamlit` for building the web app
* `google.generativeai` for generating responses
* `sqlite3` for interacting with the SQLite database
* Python 3.8 or higher for scripting

## Contact
For any queries, reach out to konashankar097@gmail.com