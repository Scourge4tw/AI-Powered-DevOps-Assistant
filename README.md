# AI-Powered DevOps Assistant

An AI-driven DevOps platform that automates CI/CD failure analysis by integrating GitHub Actions, FastAPI, React, Ollama, and Docker. The system retrieves workflow logs, analyzes failures using a Large Language Model (TinyLlama), and provides actionable debugging recommendations through a web dashboard.

---

## Features

* Automated GitHub Actions failure analysis
* AI-powered root cause detection using TinyLlama
* FastAPI backend for workflow processing
* React dashboard for visualizing analysis results
* GitHub API integration for workflow log retrieval
* Docker containerization
* Docker Compose orchestration
* Swagger API documentation
* Webhook-ready architecture for real-time automation

---

## System Architecture

```text
GitHub Actions
       │
       ▼
GitHub API
       │
       ▼
FastAPI Backend
       │
       ▼
Ollama (TinyLlama)
       │
       ▼
AI Root Cause Analysis
       │
       ▼
React Dashboard
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* Ollama
* TinyLlama
* Requests
* Pydantic

### Frontend

* React.js
* Axios

### DevOps & Infrastructure

* Docker
* Docker Compose
* GitHub Actions
* GitHub API
* ngrok

---

## Project Structure

```text
AI-Powered-DevOps-Assistant/
│
├── ai-devops-backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── ai-devops-frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
├── ai-devops-demo/
│   ├── app.py
│   ├── requirements.txt
│   └── .github/workflows/
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## Workflow

1. A GitHub Actions workflow fails.
2. The backend retrieves workflow logs through the GitHub API.
3. Logs are sent to TinyLlama via Ollama.
4. The LLM identifies the root cause and suggests fixes.
5. Analysis results are displayed on the React dashboard.

---

## Running the Project

### Backend

```bash
cd ai-devops-backend
uvicorn main:app --reload
```

### Frontend

```bash
cd ai-devops-frontend
npm install
npm start
```

### Docker

```bash
docker compose up
```

---

## API Documentation

After starting the backend:

```text
http://localhost:8000/docs
```

Swagger UI provides interactive testing for all available endpoints.

---

## Current Capabilities

* Analyze CI/CD workflow failures
* Detect dependency-related errors
* Generate AI-assisted debugging suggestions
* Retrieve GitHub workflow information
* Visualize results through a web interface
* Containerized deployment using Docker

---

## Future Enhancements

* GitHub Webhook Integration
* Real-Time Failure Notifications
* Slack/Discord Alerts
* RAG-Based DevOps Knowledge Retrieval
* Multi-Repository Monitoring
* Historical Workflow Analytics
* Kubernetes Deployment
* Self-Healing CI/CD Pipelines

---

## Resume Highlights

* Built an AI-powered DevOps platform integrating React, FastAPI, Docker, GitHub Actions, and Ollama.
* Automated CI/CD failure diagnosis through LLM-based root cause analysis.
* Designed a full-stack architecture with containerized deployment workflows.
* Integrated GitHub APIs for workflow monitoring and log retrieval.

---

## Author

**Mrinal Kumar**

Computer Science Engineering | Full Stack Development | AI/ML | DevOps
