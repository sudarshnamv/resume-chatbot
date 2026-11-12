# AI-Powered Resume Chatbot (RAG-Based)

An AI-powered chatbot that uses Retrieval-Augmented Generation (RAG) to answer questions based on information extracted from PDF resumes.

## Technologies Used

- Python
- Retrieval-Augmented Generation (RAG)
- Groq API
- ChromaDB
- LangChain
- PyPDF

## Features

- Extracts text from PDF resumes.
- Splits documents into smaller chunks for efficient processing.
- Generates and stores document embeddings in ChromaDB.
- Retrieves relevant information using semantic search.
- Uses Groq LLM to generate context-aware responses.
- Answers questions based on the content of the uploaded resume.

## How It Works

1. **PDF Loading:** Extracts text from the uploaded resume.
2. **Text Chunking:** Divides the extracted text into smaller chunks.
3. **Embedding & Storage:** Converts text into vector embeddings and stores them in ChromaDB.
4. **Retrieval:** Finds relevant resume content based on the user's question.
5. **Generation:** Sends the retrieved context to Groq to generate an answer.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sudarshnamv/resume-chatbot.git
cd resume-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install groq python-dotenv chromadb langchain langchain-community langchain-text-splitters
```

Install any additional packages required by the application.

### 4. Configure the API key

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your own Groq API key. Never upload your `.env` file.

### 5. Add your resume

Place your PDF resume in the project folder and use its filename in the application.

### 6. Run the application

```bash
python resume_chatbot.py
```

## GitHub Repository

https://github.com/sudarshnamv/resume-chatbot
