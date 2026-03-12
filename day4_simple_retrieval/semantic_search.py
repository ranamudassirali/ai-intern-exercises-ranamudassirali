from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# -----------------------------
# Step 1: Load documents
# -----------------------------
with open("documents.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

# -----------------------------
# Step 2: Load queries
# -----------------------------
with open("queries.txt", "r", encoding="utf-8") as f:
    queries = [line.strip() for line in f.readlines() if line.strip()]

# -----------------------------
# Step 3: Load embedding model
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Step 4: Generate document embeddings
# -----------------------------
doc_embeddings = model.encode(documents)

# -----------------------------
# Step 5: Process each query
# -----------------------------
results_output = []

for query in queries:

    # Encode query
    query_embedding = model.encode([query])

    # Compute similarity
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

    # Find best match
    top_indices = np.argsort(similarities)[::-1][:3]

print(f"\nQuery: {query}")
print("Top 3 Results:")

for rank, idx in enumerate(top_indices, start=1):
    print(f"{rank}. {documents[idx]} (score: {similarities[idx]:.2f})")

    # Store result
    result_text = f"""Query: {query}
Retrieved Document:
{documents[idx]}
------------------------------"""

    print(result_text)

    results_output.append(result_text)

# -----------------------------
# Step 6: Save results
# -----------------------------
with open("results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results_output))
