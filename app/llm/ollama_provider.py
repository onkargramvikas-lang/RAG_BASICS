from langchain_ollama import OllamaLLM


def get_ollama_llm(model_name):

    return OllamaLLM(
        model=model_name
    )