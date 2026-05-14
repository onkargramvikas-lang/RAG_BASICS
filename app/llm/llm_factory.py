from app.llm.config import (
    LLM_PROVIDER,
    MODEL_NAME
)

from app.llm.groq_provider import get_groq_llm

from app.llm.ollama_provider import get_ollama_llm


def get_llm():

    if LLM_PROVIDER == "groq":

        return get_groq_llm(MODEL_NAME)

    elif LLM_PROVIDER == "ollama":

        return get_ollama_llm(MODEL_NAME)

    else:

        raise ValueError(
            f"Unsupported provider: {LLM_PROVIDER}"
        )