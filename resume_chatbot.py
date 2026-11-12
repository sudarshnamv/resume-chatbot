import os
from pyexpat import model
from xml.parsers.expat import model
import chromadb
from dotenv import load_dotenv
from groq import Groq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client= Groq(api_key=api_key)

client_db=chromadb.PersistentClient(path="./chroma_db")
collection=client_db.get_or_create_collection(name="resume")
loader= PyPDFLoader("Resume.pdf")
resume=loader.load()
print("Resume uploaded!")
print("Number of pages in the resume is:",len(resume))
Splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
chunks= Splitter.split_documents(resume)
print("Total chunks:",len(chunks))
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
for i, chunks in enumerate(chunks):
    collection.add(resume=chunks.page_content,ids=[str(i)])
print("stored.")

question=input("Type in a question:")

result=collection.query(
    query_texts=[question],
    n_results=3
)
Context="/n".join(result["documents"][0])
print("Recieved")

prompt= f"""
Answer the qution by only using the context below.
Context:
{Context}
Question:
{question}
Answer:
"""
response=client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "user", "context":prompt}

    ],
    temperature=0
)
print("\nAnswer:")
print(response.choices[0].message.content)