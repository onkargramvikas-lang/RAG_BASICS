import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq


load_dotenv()


def get_groq_llm(model_name):

    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name=model_name
    )