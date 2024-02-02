# Import necessary libraries
from openai import OpenAI
import streamlit as st

# Set page configuration and title
st.set_page_config(
    page_title="ChatBot App"
)

# Display a success message in the sidebar for page selection
st.sidebar.success("Select a page")

# Set the main title of the app
st.title("ChatBot Interface")

# Initialize OpenAI client with API key
client = OpenAI(api_key="")
    
#"""
#elif st.cache_data["messages"] != None:
 #   st.session_st.messages = [st.cache_data["messages"]]
#"""
    
# Check if "openai_model" and "messages" are present in the session state, and initialize if not
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo" # gpt-3.5-turbo - base model, can switch off into hugging face based on model name

if "messages" not in st.session_state:
    st.session_state.messages = []



# Doc Source for compound statements: https://docs.python.org/3/reference/compound_stmts.html
# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input as a prompt for the chatbot
if prompt := st.chat_input("Go ahead! Ask me a question: "):
    # Append user message to the session state messages
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in the chat UI
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from the chatbot using OpenAI
    with st.chat_message("assistant"):
        # Placeholder to display the chatbot's response dynamically
        message_placeholder = st.empty()
        full_response = ""
        
        # Iterate over the chat completions stream from OpenAI
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            # Update the full response dynamically
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        
        # Display the final full response
        message_placeholder.markdown(full_response)
    
    # Append assistant's response to the session state messages
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    