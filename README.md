# 🤖 AI Assistant using LangChain + Groq

An interactive AI-powered web application that generates intelligent responses based on user queries using dynamic prompt engineering. The application features a ChatGPT-like interface with conversation memory and is built using LangChain and Groq API.

---

## 🚀 Features

- 💬 Chat-based conversational interface
- 🧠 Maintains chat history (session memory)
- ⚡ Fast responses using Groq LLM
- 🧩 Modular architecture (prompt + chain separation)
- 🎯 Dynamic prompt engineering
- 🌐 Web UI built with Streamlit


## ⚙️ Tech Stack

- **Programming Language:** Python  
- **LLM Framework:** LangChain  
- **LLM Provider:** Groq API (LLaMA3 model)  
- **Frontend/UI:** Streamlit  
- **Environment Management:** python-dotenv  
- **Version Control:** Git & GitHub  

---

## 🧠 How It Works

1. User enters a query in the chat interface  
2. The input is passed into a **Prompt Template**  
3. LangChain processes the prompt using a chain  
4. The request is sent to the Groq LLM  
5. The model generates a response  
6. The response is displayed and stored in session memory  

---
