from langchain_groq import ChatGroq
from src.prompt import get_prompt
import os

def create_chain():
    prompt = get_prompt()

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )

    # NEW STYLE (no LLMChain)
    chain = prompt | llm

    return chain