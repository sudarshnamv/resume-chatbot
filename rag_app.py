
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load API key
load_dotenv()

# 1. Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print("PDF loaded successfully!")

# 2. Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("Total chunks:", len(chunks))

# 3. Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Store chunks in ChromaDB
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_rag_db"
)

print("Documents stored in ChromaDB!")

# 5. Retrieve relevant documents
question = input("\nAsk a question about your PDF: ")

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

relevant_docs = retriever.invoke(question)

context = "\n\n".join(
    doc.page_content for doc in relevant_docs
)

# 6. Create prompt
prompt = ChatPromptTemplate.from_template("""
Answer the question using only the context below.

If the answer is not available in the context,
say you don't know.

Context:
{context}

Question:
{question}
""")

# 7. Connect Groq
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# 8. Generate answer
chain = prompt | llm

response = chain.invoke({
    "context": context,
    "question": question
})

print("\nAI Answer:")
print(response.content)
