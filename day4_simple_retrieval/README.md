# Day 4 – Simple Retrieval with Embeddings (Mini RAG System)

## 📌 Project Overview

This project demonstrates the **retrieval component of a Retrieval-Augmented Generation (RAG) system** using Python.

Modern AI systems such as ChatGPT, Perplexity AI, and Notion AI use RAG pipelines to retrieve relevant information from documents before generating answers. Instead of relying only on the training data of Large Language Models (LLMs), RAG systems allow models to access **external knowledge sources** such as documents, PDFs, databases, and company knowledge bases.

In this project, we implement a **simple semantic search system** that retrieves the most relevant document for a given query using **embeddings and cosine similarity**.

The focus of this exercise is **retrieval**, which is one of the most important components of modern AI systems.

---

# 🧠 What is Retrieval-Augmented Generation (RAG)?

Large Language Models (LLMs) have some limitations:

* They may **hallucinate incorrect information**
* Their knowledge is **limited to their training data**
* They cannot access **private documents or company data**
* They have a **knowledge cutoff date**

RAG solves these problems by combining:

1. **Information Retrieval System** – finds relevant documents
2. **Language Model (LLM)** – generates responses using those documents

Typical RAG pipeline:

User Query
↓
Search relevant documents
↓
Retrieve context
↓
Provide context to LLM
↓
LLM generates grounded answer

This project focuses on implementing the **retrieval stage of this pipeline**.

---

# 🎯 Objective

The objective of this assignment is to build a Python script that:

1. Converts text documents into **embeddings**
2. Converts a user query into an **embedding**
3. Computes **cosine similarity** between query and documents
4. Retrieves the **most relevant document**

Example:

Documents:

* Transformers use self-attention for sequence modeling.
* Diffusion models generate images by gradually removing noise.
* Embeddings convert text into vectors representing semantic meaning.

Query:

What are embeddings?

Expected Output:

Most relevant document:
Embeddings convert text into vectors representing semantic meaning.

---

# 🏗 Project Structure

ai-intern-exercises
│
└── day4_simple_retrieval
    ├── semantic_search.py
    ├── documents.txt
    ├── queries.txt
    ├── results.txt
    └── README.md

### File Descriptions

**semantic_search.py**
Main Python script that performs semantic search using embeddings.

**documents.txt**
Contains the dataset of documents used for retrieval. Each line represents a document.

**queries.txt**
Contains sample queries used to test the retrieval system.

**results.txt**
Stores the retrieved documents for each query after running the program.

**README.md**
Project documentation explaining the concept, setup, and implementation.

---

# ⚙️ Technologies Used

This project uses the following technologies:

Python
Sentence Transformers
Scikit-learn
NumPy

### Libraries Used

| Library               | Purpose                      |
| --------------------- | ---------------------------- |
| sentence-transformers | Convert text into embeddings |
| scikit-learn          | Compute cosine similarity    |
| numpy                 | Numerical operations         |

---

# 📦 Installation

Install the required dependencies using pip:

```
pip install sentence-transformers scikit-learn numpy
```

---

# 📄 Documents Dataset

The file **documents.txt** contains a collection of short documents on different topics such as:

* Machine Learning
* Artificial Intelligence
* Programming
* Space
* Sports
* Cooking

Example documents:

Machine learning algorithms learn patterns from data to make predictions or decisions without being explicitly programmed.

Neural networks are inspired by the human brain and consist of layers of interconnected neurons that process information.

The attention mechanism allows models to focus on the most important parts of the input when making predictions.

Large language models are trained on massive text datasets to understand and generate human-like language.

Reinforcement learning is a type of machine learning where agents learn by interacting with an environment and receiving rewards.

Astronauts travel to space using spacecraft designed to survive extreme conditions beyond Earth's atmosphere.

The solar system consists of the Sun and the celestial objects that orbit around it, including planets and asteroids.

Football is one of the most popular sports in the world and is played by two teams of eleven players.

Basketball requires teamwork, quick movement, and accurate shooting to score points against the opposing team.

Cooking pasta requires boiling water, adding pasta, and cooking it until it becomes tender.

Baking bread involves mixing flour, water, yeast, and salt, then allowing the dough to rise before baking.

Cybersecurity focuses on protecting computer systems and networks from digital attacks.

Databases store and organize large amounts of structured information for easy access and management.

Cloud computing allows users to store data and run applications on remote servers instead of local computers.

Artificial intelligence enables machines to perform tasks that normally require human intelligence.

Each line in the file represents **one document**.

---

# 🔍 How the System Works

The semantic search system follows these steps:

## 1️⃣ Load Documents

Documents are loaded from `documents.txt`.

Each line is treated as a separate document.

---

## 2️⃣ Generate Document Embeddings

Each document is converted into a vector using the **Sentence Transformers model**:

`all-MiniLM-L6-v2`

Example embedding vector:

[0.12, -0.45, 0.98, ...]

These vectors capture the **semantic meaning of the text**.

---

## 3️⃣ Encode the Query

The user query is also converted into an embedding vector using the same model.

Example query:

What are embeddings?

---

## 4️⃣ Compute Similarity

We compare the query embedding with all document embeddings using **cosine similarity**.

Cosine similarity measures how similar two vectors are based on their angle.

Higher similarity score means the documents are **more semantically related** to the query.

---

## 5️⃣ Retrieve the Most Relevant Document

The document with the highest similarity score is selected as the result.

The system finds the index of the best document using:

`numpy.argmax()`

---

# ▶️ Running the Program

Run the program using:

```
python semantic_search.py
```

The script will:

1. Load documents
2. Generate embeddings
3. Convert queries into embeddings
4. Compute similarity scores
5. Retrieve the most relevant document
6. Save results in `results.txt`

---

# 📝 Example Output

Example output stored in **results.txt**:

Query: What are embeddings?
Retrieved Document:
Large language models are trained on massive text datasets to understand and generate human-like language.
------------------------------
Query: What are embeddings?
Retrieved Document:
Neural networks are inspired by the human brain and consist of layers of interconnected neurons that process information.
------------------------------
Query: What are embeddings?
Retrieved Document:
The attention mechanism allows models to focus on the most important parts of the input when making predictions.
------------------------------

# ⭐ Bonus Features (Optional)

Possible improvements for this project:

* Retrieve **Top 3 most relevant documents**
* Display **similarity scores**
* Accept **user input queries from the terminal**
* Store embeddings in a **vector database like FAISS or Chroma**
* Convert this project into a **full RAG system**

Example enhanced output:

Top 3 Results:

Query: What are embeddings?
Retrieved Document:
Large language models are trained on massive text datasets to understand and generate human-like language.
------------------------------
Query: What are embeddings?
Retrieved Document:
Neural networks are inspired by the human brain and consist of layers of interconnected neurons that process information.
------------------------------
Query: What are embeddings?
Retrieved Document:
The attention mechanism allows models to focus on the most important parts of the input when making predictions.
------------------------------

---

# 🚀 Learning Outcomes

After completing this assignment, you will understand:

* What **embeddings** are
* How **semantic search** works
* How **vector similarity** is computed
* How AI systems retrieve knowledge from documents
* The **core retrieval component of RAG systems**

These concepts are widely used in modern AI systems such as:

* ChatGPT document search
* Notion AI
* GitHub Copilot Chat
* AI knowledge assistants

---

# 🔮 Future Improvements

This mini-project can be extended into a full **RAG pipeline** by adding:

* Document chunking
* Vector databases (FAISS / Pinecone / Chroma)
* Context injection into LLM prompts
* Answer generation using LLMs
* Source citations

---

# 👨‍💻 Author

AI Internship Exercise
Day 4 – Retrieval with Embeddings

This project demonstrates the **core retrieval mechanism used in modern Retrieval-Augmented Generation (RAG) systems**.
