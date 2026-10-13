from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# 1. Set project paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = BASE_DIR / "documents"
CHROMA_DIR = BASE_DIR / "chroma_db"


# --------------------------------------------------
# 2. Load the embedding model
# --------------------------------------------------

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# --------------------------------------------------
# 3. Initialize the local vector database
# --------------------------------------------------

client = chromadb.PersistentClient(
    path=str(CHROMA_DIR)
)

collection = client.get_or_create_collection(
    name="business_documents",
    metadata={"hnsw:space": "cosine"}
)


# --------------------------------------------------
# 4. Load and index business documents
# --------------------------------------------------

def load_documents():
    """Load text files and store their content in ChromaDB."""

    if not DOCUMENTS_DIR.exists():
        return f"Documents folder not found: {DOCUMENTS_DIR}"

    documents = []
    metadatas = []
    ids = []

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        try:
            text = file_path.read_text(
                encoding="utf-8"
            ).strip()

            if not text:
                continue

            # Store each complete text file as one document.
            documents.append(text)

            metadatas.append({
                "source": file_path.name
            })

            ids.append(file_path.stem)

        except OSError as error:
            print(
                f"Could not read {file_path.name}: {error}"
            )

    if not documents:
        return "No readable text documents found."

    # Generate embeddings for the documents.
    embeddings = embedding_model.encode(
        documents,
        normalize_embeddings=True
    ).tolist()

    # Add new documents or update existing documents.
    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )

    return f"Loaded {len(documents)} business documents."


# --------------------------------------------------
# 5. Search relevant business documents
# --------------------------------------------------

def search_documents(question, top_k=3):
    """Retrieve relevant, unique business documents."""

    if not question or not question.strip():
        return []

    # Index documents if the collection is empty.
    if collection.count() == 0:
        load_documents()

    total_documents = collection.count()

    if total_documents == 0:
        return []

    # Convert the question into an embedding.
    query_embedding = embedding_model.encode(
        [question],
        normalize_embeddings=True
    ).tolist()

    # Search the vector database.
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=min(top_k, total_documents),
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    matches = []
    seen_sources = set()

    result_documents = results.get(
        "documents", [[]]
    )[0]

    result_metadatas = results.get(
        "metadatas", [[]]
    )[0]

    result_distances = results.get(
        "distances", [[]]
    )[0]

    # Remove duplicate results from the same source file.
    for document, metadata, distance in zip(
        result_documents,
        result_metadatas,
        result_distances
    ):
        source = metadata.get(
            "source", "Unknown"
        )

        if source in seen_sources:
            continue

        seen_sources.add(source)

        matches.append({
            "text": document,
            "source": source,
            "distance": distance
        })

    return matches