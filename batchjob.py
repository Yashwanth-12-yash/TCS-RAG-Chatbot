from langchain_community.document_loaders import PyPDFLoader
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
#step1:load tcs report pdf file, store into documents
file_path= os.path.join("documents","tcsreport.pdf")
loader=PyPDFLoader(file_path)
documents = loader.load()
print(len(documents))

#step2: convert documents to smaller chunks
text_splitter= RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
mychunks =text_splitter.split_documents(documents)
print('total chunks:',len(mychunks))

#step3: create embedding model
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
#step4: create faiss db

index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))
vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

#step5: store our chunks into vector db
vector_store.add_documents(mychunks)
print("sucessfully created vector db")

#step 6: store vector store [db] permanently
vector_store.save_local("tcs_doc_index")
print("sucessfully stored vector db locally")