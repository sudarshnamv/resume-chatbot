
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key from .env
load_dotenv()

# Initialize the Groq model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# Ask a question
response = llm.invoke(
    "What is LangChain? Explain in simple words."
)

# Print the answer
print(response.content)
