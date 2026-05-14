# RAG Basics

A simple Retrieval-Augmented Generation (RAG) project demonstrating document loading, text splitting, and basic RAG pipeline implementation using LangChain.

## Features

- PDF document loading using PyPDFLoader
- Text splitting with RecursiveCharacterTextSplitter
- Vector store integration for document retrieval
- Modular architecture for ingestion and retrieval components

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/RAG_BASICS.git
   cd RAG_BASICS
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist, install the main packages:
   ```bash
   pip install langchain langchain-community langchain-core sentence-transformers transformers torch chromadb
   ```

## Setup

### Adding the Model

This project uses Hugging Face models for embeddings and language generation. You have two options:

#### Option 1: Use Pre-trained Models (Recommended for beginners)

1. **Embedding Model:** The project uses `sentence-transformers` for document embeddings. It's already included in the dependencies.

2. **Language Model:** For text generation, you can use models from Hugging Face:

   - **Small model (fast, less accurate):**
     ```python
     from transformers import pipeline
     generator = pipeline('text-generation', model='distilgpt2')
     ```

   - **Larger model (slower, more accurate):**
     ```python
     from transformers import pipeline
     generator = pipeline('text-generation', model='microsoft/DialoGPT-medium')
     ```

#### Option 2: Custom Model Setup

1. **Download a model from Hugging Face:**
   ```python
   from transformers import AutoTokenizer, AutoModelForCausalLM
   
   model_name = "microsoft/DialoGPT-medium"  # or any other model
   tokenizer = AutoTokenizer.from_pretrained(model_name)
   model = AutoModelForCausalLM.from_pretrained(model_name)
   ```

2. **For embeddings:**
   ```python
   from sentence_transformers import SentenceTransformer
   embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
   ```

### Environment Variables

Create a `.env` file in the root directory for API keys or model paths:

```env
# If using OpenAI API (optional)
OPENAI_API_KEY=your_api_key_here

# Hugging Face token (if needed for private models)
HUGGINGFACE_TOKEN=your_token_here
```

## Usage

1. **Prepare your data:**
   - Place PDF files in the `data/raw/` directory

2. **Run the ingestion pipeline:**
   ```bash
   python main.py
   ```

   This will:
   - Load PDF documents
   - Split text into chunks
   - Create embeddings
   - Store in vector database

3. **Query the system:**
   Modify `main.py` to include retrieval and generation logic, or create a new script:

   ```python
   from app.ingestion.loader import load_documents
   from app.ingestion.splitter import split_documents
   from sentence_transformers import SentenceTransformer
   import chromadb

   # Load and process documents
   docs = load_documents("path/to/your/document.pdf")
   chunks = split_documents(docs)

   # Create embeddings
   embedder = SentenceTransformer('all-MiniLM-L6-v2')
   embeddings = embedder.encode([chunk.page_content for chunk in chunks])

   # Store in vector DB
   client = chromadb.PersistentClient(path="./vectorstore")
   collection = client.get_or_create_collection("documents")
   collection.add(
       embeddings=embeddings,
       documents=[chunk.page_content for chunk in chunks],
       ids=[str(i) for i in range(len(chunks))]
   )

   # Query
   query = "Your question here"
   query_embedding = embedder.encode([query])
   results = collection.query(query_embeddings=query_embedding, n_results=5)
   ```

## Project Structure

```
RAG_BASICS/
├── app/
│   ├── ingestion/
│   │   ├── loader.py          # Document loading utilities
│   │   └── splitter.py        # Text splitting utilities
│   └── retrieval/             # Retrieval components (to be implemented)
├── data/
│   └── raw/                   # Raw data files (PDFs, etc.)
├── vectorstore/               # Vector database storage
├── main.py                    # Main entry point
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
├── .vscode/                   # VS Code settings
│   └── settings.json
└── README.md                  # This file
```

## Configuration

- **Chunk Size:** Modify `chunk_size` in `splitter.py` (default: 500)
- **Overlap:** Adjust `chunk_overlap` in `splitter.py` (default: 50)
- **Embedding Model:** Change the model in your scripts for different embedding quality/speed trade-offs

## Troubleshooting

- **Import Errors:** Ensure you're using the correct virtual environment and all dependencies are installed
- **Model Download Issues:** Check your internet connection and Hugging Face token if using private models
- **Memory Issues:** For large models, ensure you have sufficient RAM (16GB+ recommended)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [LangChain](https://www.langchain.com/) for the RAG framework
- [Hugging Face](https://huggingface.co/) for pre-trained models
- [ChromaDB](https://www.trychroma.com/) for vector storage