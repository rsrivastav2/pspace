from sentence_transformers import SentenceTransformer
import psycopg2
import numpy as np
import faiss

# Load local model
model_path = r"/path/to/all-mpnet-base-v2"  # folder containing model files
model = SentenceTransformer(model_path)

def get_data_from_postgres():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="your_database",
        user="your_user",
        password="your_password"
    )
    cursor = conn.cursor()

    # Select all the columns you need
    cursor.execute("SELECT id, description, category, price FROM your_table;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows  # List of tuples (id, description, category, price)

def build_faiss_index(rows):
    # We will embed only the description column (index 1)
    texts = [row[1] for row in rows]
    embeddings = model.encode(texts, convert_to_numpy=True)

    # Normalize for cosine similarity
    faiss.normalize_L2(embeddings)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # Inner product = cosine similarity for normalized vectors
    index.add(embeddings)

    return index, rows

def semantic_search(user_prompt, index, rows, top_k=5):
    query_embedding = model.encode([user_prompt], convert_to_numpy=True)
    faiss.normalize_L2(query_embedding)

    distances, indices = index.search(query_embedding, top_k)

    # Return full rows
    results = []
    for idx in indices[0]:
        results.append(rows[idx])  # Full tuple from DB
    return results

if __name__ == "__main__":
    rows = get_data_from_postgres()
    index, rows_list = build_faiss_index(rows)

    prompt = input("Enter your search query: ")
    matches = semantic_search(prompt, index, rows_list)

    print("\nTop matching results:")
    for row in matches:
        # row = (id, description, category, price)
        print(f"ID: {row[0]}, Description: {row[1]}, Category: {row[2]}, Price: {row[3]}")

