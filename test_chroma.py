
import chromadb

# 1. Create a persistent database
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# 2. Create a collection
collection = client.get_or_create_collection(
    name="my_first_collection"
)

# 3. Add documents
collection.add(
    documents=[
        "Python is a programming language.",
        "Java is an object-oriented programming language.",
        "ChromaDB is a vector database.",
        "Artificial intelligence helps machines perform intelligent tasks."
    ],
    ids=["1", "2", "3", "4"]
)

print("Documents added successfully!")

# 4. Search documents
results = collection.query(
    query_texts=["Tell me about programming"],
    n_results=2
)

# 5. Display results
print("\nSearch Results:")

for document in results["documents"][0]:
    print("-", document)

