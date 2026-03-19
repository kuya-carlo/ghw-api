# GHW API

A small **FastAPI** project built for **MLH Global Hack Week**. It includes a minimal REST API for creating and listing "challenges", along with Docker support, a VS Code devcontainer, tests, and GitHub Actions.

## 🚀 Features

- FastAPI-based JSON REST API
- In-memory storage (no database needed)
- Docker + Docker Compose support
- VS Code DevContainer config
- Pytest test suite
- GitHub Actions CI workflow

---

## ✅ Getting Started (Local)

### Prerequisites

- Python 3.12+
- pip

### Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then open: http://localhost:8000/docs

---

## 🐳 Docker

### Build and run

```bash
docker build -t ghw-api .
docker run --rm -p 8000:8000 ghw-api
```

### With docker-compose

```bash
docker compose up --build
```

---

## 🧪 Tests

```bash
pytest
```

---

## 🧠 API Endpoints & OpenAPI

The API is documented automatically via OpenAPI:

- `GET /openapi.json` - OpenAPI schema (same as `openapi.json` in the repo)
- `GET /docs` - Swagger UI
- `GET /redoc` - ReDoc UI

### Available endpoints

- `GET /` - health check
- `GET /challenges` - list challenges
- `POST /challenges` - create a challenge
- `GET /challenges/{id}` - fetch a challenge by id

---

## 🧑‍💻 DevContainer

Open this repository in VS Code and choose *Reopen in Container* (via the Command Palette). The container will install dependencies from `requirements.txt`.
