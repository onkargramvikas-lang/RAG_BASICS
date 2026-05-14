from app.retrieval.retriever import retrieve_chunks

from app.llm.llm_factory import get_llm


def ask_question(question):

    # Retrieve relevant chunks
    docs = retrieve_chunks(question)

    # Combine retrieved chunks into context
    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    # Prompt template
    prompt = f"""

You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not available in the context, say:
'I could not find the answer in the document.'

Keep the answer clear and concise.

Context:
{context}

Question:
{question}

Answer:

"""

    # Get LLM dynamically from factory
    llm = get_llm()

    # Generate response
    response = llm.invoke(prompt)

    # Handle different provider response formats
    if hasattr(response, "content"):
        return response.content
    
    return str(response)
    

    


