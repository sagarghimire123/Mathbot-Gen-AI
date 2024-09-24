import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define system message
SYSTEM_MESSAGE = "You are a Math expert with PHD level in any area such as Arethmetic, Geometry, Alzebra, Calculus and so on. Only answer the math related questions only."

# Function to get response from OpenAI API
def get_response(messages):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Use the correct model name
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": messages}
        ]
    )

    return response.choices[0].message.content

# Streamlit app
st.title("Mechanic Chatbot")

if 'history' not in st.session_state:
    st.session_state.history = []

# Input box for user messages
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        st.session_state.history.append(f"You: {user_input}")
        prompt = SYSTEM_MESSAGE + "\n" + "\n".join(st.session_state.history)
        response = get_response(user_input)  # Pass user_input instead of prompt
        st.session_state.history.append(f"AI: {response}")
        user_input = ""  # Clear input box after sending

# Display chat history
for line in st.session_state.history:
    st.write(line)
