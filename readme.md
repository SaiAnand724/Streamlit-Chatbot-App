Streamlit Chatbot App

This application  is a simple chatbot built using the streamlit library. 

The chatbot can respond to user queries using the openai gpt-3.5-turbo language model.

There is a login form that the user needs to fill out in order to access the chat functionality of the app.


Streamlit Docs: https://docs.streamlit.io/library/api-reference

PowerShell prompts
1. python -m venv .venv - sets the virtual environment (name of this venv is .venv)
2. python -m pip install {dependencies}
    - langchain[llms], openai, tiktoken, python-dotenv, streamlit, streamlit-authenticator
    - For databases: [MySQL - mysqlclient, SQLAlchemy], [MongoDB - pymongo]
3. .venv/Scripts/activate - activates virtual environment
    - deactivate - leaves the virtual environment and returns to working directory
4. python -m streamlit run {streamlit app main python file}