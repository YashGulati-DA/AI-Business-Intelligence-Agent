from document_search import (
    load_documents,
    search_documents
)

# Load the documents
print(load_documents())

# Search for relevant information
question = "What does the shipping policy say about delivery dates?"

results = search_documents(question)

print("\nSearch Results:\n")

for result in results:
    print("Source:", result["source"])
    print("Text:", result["text"])
    print("-" * 50)