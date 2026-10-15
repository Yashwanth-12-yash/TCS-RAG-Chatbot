# 🤖 TCS RAG Chatbot

An AI-powered chatbot built using Retrieval-Augmented Generation (RAG) architecture. The chatbot answers questions based only on the contents of a PDF document by retrieving relevant information from a FAISS vector database and generating responses using Google's Gemini model.

## Features

- Upload and process PDF documents
- Split documents into text chunks
- Generate embeddings using MPNet
- Store embeddings in FAISS Vector Database
- Retrieve relevant document chunks
- Generate accurate responses using Gemini
- REST API developed using Flask

## Tech Stack

- Python
- Flask
- LangChain
- Hugging Face Embeddings (all-mpnet-base-v2)
- FAISS
- PyPDF
- Google Gemini API

## Project Workflow

1. Load PDF
2. Split PDF into chunks
3. Generate embeddings
4. Store vectors in FAISS
5. Receive user question
6. Retrieve relevant chunks
7. Send retrieved context to Gemini
8. Return the generated response

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/TCS-RAG-Chatbot.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Generate Vector Database

```bash
python batchjob.py
```

Run the application

```bash
python app.py
```

## API Endpoint

```
POST /tcs
```

Example Request

```json
{
    "tcs question":"What is the leave policy?"
}
```

## Future Enhancements

- Multiple PDF support
- Chat history
- Streamlit Web Interface
- User Authentication
- Offline LLM Support

## Author

Vignesh
