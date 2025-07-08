# 📄 PDF RAG-based Chatbot

This project is a **Retrieval-Augmented Generation (RAG)** chatbot that allows users to ask questions about a PDF document. It combines **FastAPI**, **ChromaDB**, **HuggingFace Embeddings**, and **OpenAI LLMs**. Each document is preprocessed using **NER (Named Entity Recognition)** and **Topic Modeling**, adding metadata to improve retrieval quality.

---

## 🚀 Features

- 📚 **PDF Document Loader** (via `PyPDFLoader`)
- 🧩 **Chunking** with overlap for context retention
- 🧠 **Named Entity Recognition (NER)** using spaCy
- 🧠 **Topic Modeling** with Latent Dirichlet Allocation (LDA)
- 🔍 **ChromaDB** Vector Store using `langchain_chroma`
- 🤖 **Chatbot** with RAG pipeline using OpenAI's GPT models
- 🔒 **FastAPI** backend with optional SSL support
- 🐳 **Dockerized** for portable deployment

---

## 📁 Project Structure

```bash
PDF-RAG-based-Chatbot/
│
├── app.py                    # FastAPI entrypoint
├── db.py                     # Vector DB setup (Chroma)
├── ragchain.py              # RAG chain logic
├── topic_modelling.py       # Metadata generation via NER + LDA
├── llm.py                   # OpenAI LLM configuration
├── prompt.py                # Prompt template
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker container setup
├── .dockerignore
├── .gitignore
├── cert.pem                 # SSL certificate (should be gitignored)
├── cert.key                 # SSL private key (should be gitignored)
├── sample-local-pdf.pdf     # Example PDF
└── chroma_langchain_db/     # ChromaDB persisted directory
