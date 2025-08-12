import psycopg2
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="your_database",
    user="your_username",
    password="your_password"
)
cursor = conn.cursor()

# 2. Run SELECT query to fetch text data
cursor.execute("SELECT your_text_column FROM your_table;")
rows = cursor.fetchall()

# Extract just the text from each row
documents = [row[0] for row in rows]

# 3. Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 4. Encode documents
doc_embeddings = model.encode(documents, normalize_embeddings=True, show_progress_bar=True)

# 5. Create FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)  # cosine similarity
index.add(doc_embeddings)

# 6. Take user input and search
while True:
    query = input("\nEnter your search query (or type 'exit' to quit): ")
    if query.lower() == "exit":
        break

    query_embedding = model.encode([query], normalize_embeddings=True)
    k = 5  # top results
    distances, indices = index.search(query_embedding, k)

    print("\nTop Matches:")
    for idx, score in zip(indices[0], distances[0]):
        print(f"- {documents[idx]} (score: {score:.4f})")

# 7. Close DB connection
cursor.close()
conn.close()
