# RAGOON-X1

**A modular, extensible Retrieval-Augmented Generation (RAG) framework for building and experimenting with production-oriented RAG pipelines.**

RAGoon-X1 provides a modular architecture for document ingestion, chunking, embedding, hybrid retrieval, reranking, context compression, and LLM-based generation.

The framework is designed so that individual components can be replaced or extended without changing the entire pipeline.

---

## ✨ Features

* 🧩 **Modular RAG Architecture**

  * Document loading
  * Cleaning and metadata extraction
  * Chunking
  * Embedding
  * Vector storage
  * Sparse retrieval
  * Hybrid retrieval
  * Query rewriting
  * Multi-query generation
  * Cross-encoder reranking
  * Context compression
  * LLM generation

* 🔎 **Hybrid Retrieval**

  * Dense vector retrieval using Qdrant
  * Sparse retrieval using BM25
  * Combined retrieval pipeline

* 🧠 **Query Processing**

  * Query rewriting
  * Multi-query expansion
  * Retrieval from multiple query variants

* 🎯 **Reranking**

  * Cross-encoder based reranking of retrieved candidates

* 🗜️ **Context Compression**

  * Reduces retrieved context before sending it to the LLM

* ⚙️ **Configuration Driven**

  * User-facing `ragoonx.yaml`
  * Environment-variable support for secrets
  * Configurable LLM, embedding, retrieval, chunking, storage, and data settings

* 💻 **CLI Interface**

  * `init`
  * `ingest`
  * `chat`
  * `doctor`

* 🔌 **Extensible Components**

  * Factory-based component creation
  * Abstract interfaces for major pipeline components
  * New loaders, embeddings, storage backends, rerankers, and generators can be added independently

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │   Document Source   │
                         │       JSONL         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Document Loader   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Cleaning       │
                         │   + Metadata        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Chunking       │
                         │     Recursive       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Embedding      │
                         │ BAAI/bge-small-en-v1.5
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
          ┌─────────────────┐             ┌─────────────────┐
          │     Qdrant      │             │      BM25       │
          │ Dense Retrieval │             │ Sparse Retrieval│
          └────────┬────────┘             └────────┬────────┘
                   │                               │
                   └───────────────┬───────────────┘
                                   ▼
                         ┌─────────────────────┐
                         │   Hybrid Retrieval  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Query Rewriting   │
                         │   Multi-Query       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Reranking       │
                         │   Cross-Encoder     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Context Compression │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    LLM Generation  │
                         │        Groq         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                              Final Answer
```

---

## 🚀 Installation

### 📦 Install from PyPI

```bash
pip install ragoonx
```

### 🛠️ Install from Source

```bash
git clone https://github.com/saksham5k2/RAGOON-X1.git
cd RAGOON-X1

python -m venv .venv
```

#### Git Bash / Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

Install the project:

```bash
pip install -e .
```

---

## ⚙️ Configuration

Initialize the configuration:

```bash
ragoonx init
```

This creates a local `ragoonx.yaml` configuration file.

Example configuration:

```yaml
llm:
  provider: groq
  model: openai/gpt-oss-120b
  api_key: ${GROQ_API_KEY}
  base_url: https://api.groq.com/openai/v1
  temperature: 0.0
  max_tokens: 512

embedding:
  provider: huggingface
  model: BAAI/bge-small-en-v1.5

retrieval:
  top_k: 10

chunking:
  strategy: recursive
  size: 512
  overlap: 100

storage:
  provider: qdrant
  qdrant_path: storage/qdrant_store
  bm25_path: storage/bm25.pkl
  document_store: storage/documents.json

data:
  wikipedia_dump: ""
```

### 🔑 API Key

RAGoon-X1 uses an environment variable for the Groq API key.

#### Git Bash / Linux / macOS

```bash
export GROQ_API_KEY="your_groq_api_key"
```

#### Windows PowerShell

```powershell
$env:GROQ_API_KEY="your_groq_api_key"
```

> 🔒 **Never commit your API key to GitHub.**

---

## 💻 CLI Usage

### 🔧 Initialize

Create the user configuration:

```bash
ragoonx init
```

### 🩺 Run Diagnostics

Check the local installation and required resources:

```bash
ragoonx doctor
```

Example:

```text
RAGOON-X1 Diagnostics

✓ Configuration
✓ GROQ API Key
✓ Qdrant Storage
✓ BM25 Index
✓ Document Store

5/5 checks passed.
```

### 📥 Ingest Documents

RAGoon-X1 currently provides a JSONL document loader.

```bash
ragoonx ingest path/to/documents.jsonl
```

Example:

```bash
ragoonx ingest data/raw/stencore/stencore_10k.jsonl
```

The ingestion pipeline performs:

```text
Load
 ↓
Clean
 ↓
Metadata Extraction
 ↓
Document Store
 ↓
Chunking
 ↓
Embeddings
 ↓
Qdrant
 ↓
BM25
```

Example output:

```text
Indexed: Document 1 (8 chunks)
Indexed: Document 2 (4 chunks)
Indexed: Document 3 (8 chunks)
Indexed: Document 4 (9 chunks)

...

Total chunks indexed: 88
```

### 💬 Start Chat

Start an interactive RAG session:

```bash
ragoonx chat
```

Example:

```text
RAGOON-X1 Chat
Type 'exit' to quit.

> american lifeguard training course
```

The query passes through the retrieval pipeline before the final answer is generated.

---

## 🔎 Retrieval Pipeline

```text
                         User Query
                              │
                              ▼
                       Query Rewriting
                              │
                              ▼
                      Multi-Query Expansion
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             Dense Retrieval     Sparse Retrieval
                 Qdrant                BM25
                    │                   │
                    └─────────┬─────────┘
                              ▼
                       Hybrid Retrieval
                              │
                              ▼
                           Reranking
                              │
                              ▼
                     Context Compression
                              │
                              ▼
                       LLM Generation
                              │
                              ▼
                         Final Answer
```

The retrieval stack includes:

* 🔢 **Dense Embeddings:** `BAAI/bge-small-en-v1.5`
* 🗄️ **Vector Store:** Qdrant
* 🔤 **Sparse Retrieval:** BM25
* 🎯 **Reranking:** Cross-Encoder
* 🗜️ **Context Compression**
* ✏️ **Query Rewriting**
* 🔀 **Multi-Query Retrieval**

---

## 🧠 Embeddings

RAGoon-X1 currently uses:

```text
BAAI/bge-small-en-v1.5
```

The embedding model is loaded through the embedding factory, allowing the implementation to be replaced without modifying the rest of the ingestion or retrieval pipeline.

Embeddings are normalized before storage and retrieval.

---

## 🗄️ Storage

RAGoon-X1 currently uses three storage components.

### 🔵 Qdrant

Stores dense vector representations of document chunks.

```text
storage/qdrant_store/
```

### 🟢 BM25

Stores the sparse retrieval index.

```text
storage/bm25.pkl
```

### 📄 Document Store

Stores complete ingested documents.

```text
storage/documents.json
```

---

## 📁 Project Structure

```text
RAGOON-X1/
│
├── chunking/             # Chunking strategies
├── embeddings/           # Embedding models
├── generation/           # LLM generation and prompting
├── ingestion/            # Loaders, cleaning, metadata, ingestion
├── models/               # Core data models
├── rag/                  # Main RAG pipeline
├── ragoonx/              # Package, configuration and CLI
├── reranking/            # Cross-encoder reranking
├── retrieval/            # Retrieval pipeline
├── storage/              # Vector, sparse and document stores
├── tests/                # Tests
│
├── pyproject.toml
└── README.md
```

---

## 🧩 Extensibility

RAGoon-X1 is designed around interfaces and factories.

The framework can be extended with:

* 📄 New document loaders
* ✂️ New chunking strategies
* 🧠 Alternative embedding models
* 🗄️ Alternative vector databases
* 🔤 Additional sparse retrieval methods
* 🎯 Different reranking models
* 🗜️ Custom context compressors
* 🤖 Additional LLM providers
* 📝 Custom generation strategies

Individual components can be changed without rewriting the entire RAG pipeline.

---

## 📊 Validation

### 🧪 End-to-End Validation

RAGoon-X1 V2.1 has been tested as a **packaged end-user installation**, including testing from a separate virtual environment rather than relying exclusively on the development source tree.

Validation included:

* ✅ Package installation
* ✅ `ragoonx init`
* ✅ `ragoonx doctor`
* ✅ JSONL document ingestion
* ✅ Dense vector indexing
* ✅ BM25 indexing
* ✅ Hybrid retrieval
* ✅ Query rewriting
* ✅ Multi-query generation
* ✅ Cross-encoder reranking
* ✅ Context compression
* ✅ Groq-based generation
* ✅ Interactive chat

### 📈 Large-Scale Dataset Testing

The framework has been tested across **multiple datasets totaling more than 1 million documents**.

A separate 10K-document dataset was also used for detailed ingestion and end-to-end interactive testing.

> ℹ️ The **1M+ figure represents validation across multiple datasets**, rather than a single 1M-document ingestion run.

### ⚡ Example Ingestion Test

A 10-document test dataset produced:

```text
Indexed: Document 1 (8 chunks)
Indexed: Document 2 (4 chunks)
Indexed: Document 3 (8 chunks)
Indexed: Document 4 (9 chunks)
Indexed: Document 5 (17 chunks)
Indexed: Document 6 (6 chunks)
Indexed: Document 7 (10 chunks)
Indexed: Document 8 (15 chunks)
Indexed: Document 9 (6 chunks)
Indexed: Document 10 (5 chunks)

Total chunks indexed: 88
```

The end-to-end ingestion completed successfully with dense and sparse indexes generated.

---

## 📋 Requirements

* 🐍 Python 3.10+
* 🤗 Sentence Transformers
* 🤗 Transformers
* 🗄️ Qdrant Client
* 🔤 BM25
* 🔌 OpenAI-compatible Python client
* ⚙️ PyYAML
* 📦 Additional dependencies specified in `pyproject.toml`

For the complete dependency list, see:

```text
pyproject.toml
```

---

## 🛠️ Development

Clone the repository:

```bash
git clone https://github.com/saksham5k2/RAGOON-X1.git
cd RAGOON-X1
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install in editable mode:

```bash
pip install -e .
```

Run diagnostics:

```bash
ragoonx doctor
```

---

## 🤝 Contributing

Contributions, bug reports, feature requests, and improvements are welcome.

Create a feature branch:

```bash
git checkout -b feature/your-feature
```

Make your changes and run the available tests and diagnostics.

Commit your changes:

```bash
git add .
git commit -m "Describe your change"
```

Push your branch:

```bash
git push origin feature/your-feature
```

Then open a Pull Request.

---

## 📄 License

RAGoon-X1 is released under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

## 👤 Author

**Saksham**

🔗 GitHub: https://github.com/saksham5k2

⭐ Repository: https://github.com/saksham5k2/RAGOON-X1

---

## 🚀 Project Status

### RAGoon-X1 V2.1

RAGoon-X1 is an actively developed modular RAG framework focused on:

* 🧩 Reusable architecture
* 🔎 Advanced retrieval
* ⚙️ Configuration-driven usage
* 📦 Python package distribution
* 💻 CLI-based operation
* 📈 Large-scale document ingestion
* 🔌 Extensible RAG components

**Built for experimentation, extensibility, and practical RAG development.** ❤️
