
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

file = canvas.Canvas("sample.pdf", pagesize=A4)

text = file.beginText(50, 780)
text.setFont("Helvetica", 12)

content = """
ARTIFICIAL INTELLIGENCE AND PYTHON

Python is a popular programming language.

Artificial Intelligence enables machines to perform
tasks that normally require human intelligence.

Machine Learning is a branch of Artificial Intelligence.

Large Language Models are AI models that understand
and generate human language.

Vector databases store numerical representations
of information called embeddings.

ChromaDB is a vector database used for similarity search.

RAG stands for Retrieval Augmented Generation.

RAG retrieves relevant information from documents
before sending the context to a language model.

LangChain is a framework used to build applications
powered by Large Language Models.

Groq provides APIs to access language models.
"""

for line in content.strip().split("\n"):
    text.textLine(line)

file.drawText(text)
file.save()

print("Valid PDF created successfully!")
