import streamlit as st
from dotenv import load_dotenv
from src.chain import create_chain

# Load API key
load_dotenv()

st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("🤖 AI Assistant (LangChain + Groq)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input box (ChatGPT style)
user_input = st.chat_input("Ask something...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.chat_message("user").write(user_input)

    # Create chain
    chain = create_chain()

    with st.spinner("Thinking..."):
        response = chain.invoke({
            "topic": user_input,
            "difficulty": "beginner"
        })

    ai_response = response.content

    # Save AI message
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    st.chat_message("assistant").write(ai_response)