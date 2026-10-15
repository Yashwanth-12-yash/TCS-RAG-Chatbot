'''
this file contains real time job a rest api that accepts question from postman
note: question should be json format
step1: read question
step2: convert question to vector using embedding model
step3: load faiss db ->tcs_doc_index
step4: ask question faiss db, get relevant chunks
step5: make prompt with question, and context
step6: pass prompt to any free LLLms (openai,gemini, huggingface)
step7: get answer from LLMs and return to postman 
''' 
from flask import Flask,request,jsonify
from langchain_huggingface import HuggingFaceEmbeddings
import faiss
from langchain_community.vectorstores import FAISS
from google import genai
import os
app=Flask(__name__)
@app.route("/tcs",methods=["POST"])
def tcs_chatbot_api():
    data = request.get_json()
    Question = data.get("tcs question")
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    
    new_vector_store= FAISS.load_local(
        "tcs_doc_index",embeddings, allow_dangerous_deserialization=True
    )
    docs =new_vector_store.similarity_search(Question,k=10)
    
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f'''
                Answer the question using only the context below.
                if the answer is not in the context, say "I don't know".
                Question: {Question}
                context: {context}
                '''
    

    client = genai.Client(api_key="Your API Key")

    interaction = client.interactions.create(
      model="gemini-3.5-flash",
      input=prompt
)


    
    return jsonify({"gemini response":str(interaction.output_text)})

app.run()



    




    