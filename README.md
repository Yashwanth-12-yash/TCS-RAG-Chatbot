# TCS RAG Chatbot — Generative AI

A Python-based Generative AI chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer questions using information retrieved from a TCS-related PDF document.

The application combines document processing, semantic search, vector storage, and a Large Language Model (LLM) to provide context-aware answers through a Flask REST API.

## Overview

Traditional chatbots may generate answers without access to a specific knowledge base. This project uses RAG to retrieve relevant document content before generating a response.

The system indexes a PDF document, converts its text into embeddings, stores those embeddings in FAISS, and retrieves relevant passages when a user submits a question. The retrieved context is then passed to Google's Gemini model to generate a response.

## Key Features

- **PDF ingestion:** Loads the source document for processing.
- **Text chunking:** Splits document content into manageable text segments.
- **Text embeddings:** Converts document chunks and user questions into numerical vector representations.
- **Vector search:** Uses FAISS to retrieve relevant document passages.
- **Context-aware generation:** Supplies retrieved context to Gemini for answer generation.
- **REST API:** Exposes a Flask endpoint for submitting questions and receiving answers.
- **Context-grounded prompting:** Instructs the model to respond using the supplied context and acknowledge when the answer is unavailable.

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| API framework | Flask |
| RAG framework | LangChain |
| PDF processing | PyPDF / PyPDFLoader |
| Embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| Vector database | FAISS |
| Generative AI | Google Gemini API |
| API testing | Postman |

## System Architecture

```text
TCS PDF Document
       |
       v
   PDF Loading
       |
       v
  Text Chunking
       |
       v
 Embedding Model
       |
       v
 FAISS Vector Index
       |
       | Saved locally
       v
   tcs_doc_index

User Question
       |
       v
 Flask REST API
       |
       v
Question Embedding
       |
       v
 FAISS Similarity Search
       |
       v
Relevant Document Chunks
       |
       v
Question + Retrieved Context
       |
       v
 Google Gemini LLM
       |
       v
 JSON Response to Client
```

## Project Workflow

### 1. Document ingestion

The `batchjob.py` script loads the PDF document from the `documents/` directory.

### 2. Text chunking

The extracted document text is divided into smaller chunks using LangChain's `RecursiveCharacterTextSplitter`. The current configuration uses a chunk size of 1,000 characters and an overlap of 200 characters.

### 3. Embedding generation

The embedding model converts the document chunks into numerical vectors that represent their semantic content.

### 4. Vector indexing

The vectors and corresponding document chunks are stored in a FAISS index and saved locally in the `tcs_doc_index/` directory.

### 5. Question submission

The user submits a question to the Flask API using an HTTP POST request.

### 6. Relevant context retrieval

The application searches the saved FAISS index and retrieves the most relevant document chunks for the question.

### 7. Answer generation

The retrieved context and user question are combined into a prompt and sent to Google's Gemini model.

### 8. Response delivery

The generated answer is returned to the API client in JSON format.

## Project Structure

```text
TCS-RAG-Chatbot/
│
├── app.py             # Flask API and RAG question-answering logic
├── batchjob.py        # PDF processing and FAISS index creation
├── documents/
│   └── tcsreport.pdf  # Source PDF document
├── tcs_doc_index/     # Saved FAISS index and related data
└── README.md          # Project documentation
```

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version supported by the dependencies
- pip package manager
- A Google Gemini API key
- Internet access for downloading dependencies and accessing the Gemini API

### 1. Clone the repository

```bash
git clone https://github.com/Yashwanth-12-yash/TCS-RAG-Chatbot.git
cd TCS-RAG-Chatbot
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks environment activation, you can run the environment's Python executable directly or follow the official Python virtual-environment instructions.

### 3. Install dependencies

Install the packages used by the application:

```powershell
python -m pip install Flask faiss-cpu langchain-community langchain-text-splitters langchain-huggingface sentence-transformers pypdf google-genai
```

### 4. Configure the Gemini API key

Create a Gemini API key through Google AI Studio.

Set it as an environment variable in PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

Never commit API keys or other secrets to GitHub.

The application must read this environment variable when initializing the Gemini client. Do not place a real API key directly in the source code.

### 5. Prepare the vector database

Ensure that the source PDF is available at:

```text
documents/tcsreport.pdf
```

Then run:

```powershell
python batchjob.py
```

This processes the PDF and creates the local FAISS index in `tcs_doc_index/`.

Run this step again whenever the source document changes or the index needs to be rebuilt.

### 6. Start the Flask API

```powershell
python app.py
```

The API runs using the host and port configured in `app.py`.

## Testing the API with Postman

Send a POST request to:

```text
http://127.0.0.1:5000/tcs
```

Set the request body to **raw JSON**:

```json
{
  "tcs question": "What information is available in the document?"
}
```

Set the request header:

```text
Content-Type: application/json
```

A successful response follows this general format:

```json
{
  "gemini response": "The generated answer based on the retrieved document context."
}
```

The exact answer depends on the source document, the retrieved passages, and the model output.

## Security and Limitations

- Keep API keys in environment variables rather than source code.
- Only index documents you have permission to use.
- The quality of answers depends on the source document, retrieval relevance, and model behavior.
- The application is designed around the configured PDF and local FAISS index; additional document formats and user-facing interfaces would require further implementation.

## Learning Outcomes

This project demonstrates practical concepts in:

- Retrieval-Augmented Generation (RAG)
- Text embeddings and semantic retrieval
- Vector indexing with FAISS
- PDF processing and text chunking
- LLM prompt construction
- Building and testing REST APIs with Flask
- Integrating a hosted Generative AI model

## Future Enhancements

- Support multiple document formats and multiple PDFs
- Add conversation history
- Improve retrieval quality and relevance evaluation
- Add a dedicated web-based chat interface
- Implement authentication, logging, and error handling

---

**Repository:** [TCS-RAG-Chatbot](https://github.com/Yashwanth-12-yash/TCS-RAG-Chatbot)

*Project documentation should reflect the implementation and contributions accurately. Features listed as future enhancements are not claimed as completed functionality.*