
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Connect to Groq
client = Groq(api_key=api_key)

# Send a question to AI
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain Python in simple words."
        }
    ]
)

# Display AI response
print(response.choices[0].message.content)
