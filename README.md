# RAG Langchain
A production-ready RAG () system built with FastAPI, LangChain, LangServe, LangSmith, Hugging Face, and Qdrant for document processing and intelligent querying.


## Table of Contents
- [Core Features](#core-features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [API Endpoints](#api-endpoints)
- [Components](#Components)
- [Development](#development)
- [Testing](#testing)
- [Configuration](#configuration)


## Core Features
- PDF Document Processing with automatic chunking and metadata enrichment
- Vector Search using Qdrant with sentence-transformers/all-MiniLM-L6-v2 embedding model for efficient document retrieval
- Integration with google/flan-t5-base for question answering
- RESTful API with streaming support
- Docker containerization with multi-service architecture


## Tech Stack
- FastAPI + Uvicorn
- LangChain + LangServe
- Qdrant Vector Database
- Hugging Face Models ([google/flan-t5-base](https://huggingface.co/google/flan-t5-base), [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2))
- LangSmith for monitoring and debugging
- PyPDF for document processing


## Quick Start
1. Clone the repository:
```bash
git clone https://github.com/hoduy511/rag-langchain.git
cd RAG-LangChain
```

2. Create and configure your .env file with required variables:
```bash
cp .env-dev .env
```

3. Start the services using `make up` command:
```bash
make up
```


## API Endpoints
### Base URLs
- API Documentation: http://localhost:8000/docs
- Interactive Playground: http://localhost:8000/rag/playground

### Core Endpoints
- `GET /health` - Health check endpoint
- `POST /api/v1/upload` - Upload and process PDF documents
- `POST /api/v1/query` - Query the knowledge base  
- `POST /api/v1/search` - Perform similarity search


## Components
### API Layer (`src/api/`)
- FastAPI application handling HTTP requests
- Route definitions for document upload, querying, and search
- Input validation and response formatting
- CORS and middleware configuration

### Core Services (`src/services/`)
#### Document Formatter
- Text chunking with configurable size and overlap
- Metadata enrichment
- UTF-8 encoding handling
- Content cleaning and normalization

#### LLM Service
- google/flan-t5-base model integration
- Text generation pipeline configuration
- Token length management
- Model parameter optimization

#### PDF Service
- PDF document processing
- Text extraction and cleaning
- Temporary file management
- Chunk generation and storage

#### Vector Store
- Qdrant vector database integration
- Document embedding using sentence-transformers
- Similarity search functionality
- Collection management and indexing

### RAG Chain (`src/chains/`)
- LangChain implementation for question answering
- Integration with google/flan-t5-base model
- Prompt management and chain composition
- Context retrieval and response generation

### Data Models (`src/models/`)
- Pydantic schemas for request/response validation
- Data transfer object definitions
- Type hints and validation rules


## Development
Available make commands for development:
- `up`: Start all services with docker-compose
- `down`: Stop all services and remove containers
- `logs`: View container logs in follow mode
- `shell`: Open interactive shell in app container
- `clean`: Remove all containers, volumes and prune system
- `test`: Run pytest test suite
- `format`: Format Python code with autopep8 and isort
- `lint`: Run flake8 linter checks


## Testing
The project includes comprehensive tests for all components including API endpoints, RAG chain implementation, and various services.


## Configuration
### Environment Variables
- API settings
- Qdrant vector database configuration
- Model settings (google/flan-t5-base and sentence-transformers/all-MiniLM-L6-v2)
- LangChain integration parameters
- LangSmith API keys and project settings
- Hugging Face API tokens and model configurations