🚀 Ollama AI Chatbot (LangChain + Streamlit)

## 📌 Overview

This project is an interactive AI chatbot built with LangChain, Streamlit, and Ollama. It allows users to chat with an LLM (Large Language Model) locally while providing an intuitive web interface.

- 🔹 Uses LangChain for prompt handling
- 🔹 Runs Ollama LLM locally (Mistral, Llama3, Gemma, etc.)
- 🔹 Provides interactive UI with Streamlit
- 🔹 Adjustable temperature, model, and response settings

## 🛠️ Installation & Setup

### 1️⃣ Install Required Dependencies

```bash
pip install streamlit langchain ollama python-dotenv
```

### 2️⃣ Install & Run Ollama (Required)

Ollama runs LLMs locally on your machine. Download and install it from:🔗 Ollama Download

After installation, start the Ollama service:
```
ollama serve
```
### 3️⃣ Run the Chatbot

Execute the following command:
```
streamlit run test.py
```
### ⚙️ Features

- ✅ Customizable Models: Choose between llama3, mistral, gemma, etc.
- ✅ Multi-turn Chat: Keeps conversation history
- ✅ UI Customization: Dark Mode, Adjustable Temperature
- ✅ Fast Responses: Runs locally for zero-latency AI
- ✅ Open-Source & Private: No cloud dependency!

## 🖥️ Usage

### 1️⃣ Start the Ollama LLM server:
```
ollama serve
```
### 2️⃣ Run the chatbot with Streamlit:
```
streamlit run test.py
```
### 3️⃣ Enter your query in the text box and get responses!

## 📌 API & Future Enhancements

- 🔹 Voice Support (Speech-to-Text)
- 🔹 Multi-User Mode (Session-based storage)
- 🔹 File Uploads (Document Q&A with AI)

## 🤝 Contributing

- Fork the repo & clone it locally

Create a new branch:
```
git checkout -b feature-branch
```
Make your changes and commit:
```
git commit -m "Added new feature"
```
Push to GitHub:
```
git push origin feature-branch
```
Open a Pull Request 🚀


## Resources
- [Ollama Official Site](https://ollama.com/download)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Docs](https://python.langchain.com/)
