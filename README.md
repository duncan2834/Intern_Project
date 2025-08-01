# Intern_Project

```bash
INTERN_PROJECT/
├── src/
│   ├── __init__.py
│   ├── main.py                    # Entry point, FastAPI app initialization
│   ├── core/
│   │   ├── __init__.py
│   │   ├── database.py            # Database connections 
│   │   ├── embedding.py           # Embedding service 
│   │   ├── llm_classifier.py      # LLM service for deciding important message
│   │   └── dependencies.py        # FastAPI dependencies
│   ├── models/
│   │   ├── __init__.py
│   │   ├── database_models.py     # models for PostgreSQL
│   │   └── schemas.py             # Pydantic models cho request/response
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chat_service.py        # Business logic cho chat
│   │   ├── vector_service.py      # Vector search logic
│   │   └── faiss_indices/
│   │       ├── __init__.py
│   │       ├── base_index.py      # Abstract base class cho FAISS indices
│   │       ├── ivf_index.py       # IVF (Inverted File) implementation
│   │       ├── hnsw_index.py      # HNSW (Hierarchical NSW) implementation
│   │       └── pq_index.py        # Product Quantization implementation
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── chat.py            # Chat endpoints
│   │   │   ├── search.py          # Vector search endpoints
│   │   │   ├── list.py        # Message list endpoints
│   │   └── router.py               
├── tests/
│   ├── __init__.py
│   ├── test_api/
│   ├── test_services
├── .gitignore
├── README.md
└── pyproject.toml                 # Poetry/setuptools configuration
```
