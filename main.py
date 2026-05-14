from app.retrieval.rag_chain import ask_question
# from app.ingestion.pipeline import run_ingestion

# run_ingestion()

question = input("Ask a question: ")

response = ask_question(question)

print("\nAnswer:\n")

print(response)