from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Hello there! You are a helpful AI assistant."),
    ("user", "Question: {question}")
])

# Streamlit UI Setup
st.set_page_config(page_title="Ollama AI Chat", page_icon="🤖", layout="wide")

# Sidebar Settings
st.sidebar.title("⚙️ Settings")
model = st.sidebar.selectbox("Select LLM Model", ["llama3.2", "mistral", "gemma"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
top_k = st.sidebar.slider("Top-K Sampling", 1, 50, 20)
top_p = st.sidebar.slider("Top-P Sampling", 0.0, 1.0, 0.9, 0.05)
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

# Apply dark mode
if dark_mode:
    st.markdown("""
        <style>
            body { background-color: #1e1e1e; color: white; }
            .stTextInput>div>div>input { color: white; }
        </style>
    """, unsafe_allow_html=True)

# Initialize Chat
st.title("💬 Ollama AI Chatbot")
st.write("Ask me anything, and I will try my best to assist you!")

# Maintain Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input Box
input_text = st.text_input("Type your question here...")

# LLM Setup
llm = Ollama(model=model)  # Initialize Ollama with user-selected model
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Handle User Input
if input_text:
    start_time = time.time()

    with st.spinner("Thinking... 🤔"):
        response = chain.invoke({'question': input_text})

    response_time = round(time.time() - start_time, 2)

    # Display user question
    with st.chat_message("user"):
        st.markdown(input_text)

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save chat history
    st.session_state.messages.append({"role": "user", "content": input_text})
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Show response time
    st.sidebar.success(f"🕒 Response Time: {response_time} sec")

# Clear Chat Button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()
