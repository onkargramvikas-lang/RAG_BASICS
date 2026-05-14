from app.ingestion.loader import load_documents

from app.ingestion.splitter import split_documents

from app.ingestion.embedder import create_vector_store


def run_ingestion():

    documents = load_documents("data/raw/Onkar_Anand_resume.pdf")

    chunks = split_documents(documents)

    create_vector_store(chunks)

    print("Ingestion completed successfully")