# Step 1: Setup the streamlit 
import streamlit as st
import requests
BACKEND_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="MindCare AI Assistant", page_icon=":robot_face:", layout="wide")
st.title("🧠 MindCare AI Assistant")

# Step 2: Initialize the session state
# This is a dictionary that will store the conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Step 3: Enable the user to ask 
# User can enter a message and it will be added to the conversation history
if prompt := st.chat_input("What's on your mind today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = requests.post(BACKEND_URL,json={"message":prompt})

    st.session_state.messages.append({"role": "assistant", "content": f'{response.json()["response"]} WITH TOOL: [{response.json()["tool_called"]}]'})

# Step 4: Display the conversation
# This will display the conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


