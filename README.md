# GitHub Cloud Connector

A REST API connector for GitHub built with FastAPI (Python).

## Setup

1. Clone the repo
2. Create virtual env: `python -m venv venv && venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your GitHub PAT token

## Run
```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for interactive API docs.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/repos/{username}` | Fetch all repos for a user |
| GET | `/list-issues/{owner}/{repo}` | List issues in a repo |
| POST | `/create-issue` | Create a new issue |

## Authentication
Uses GitHub Personal Access Token stored in `.env` file (never hardcoded).



## Project Structure

github-connector/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   ├── routes/
│   │   ├── repos.py     # /repos endpoint
│   │   ├── issues.py    # /create-issue, /list-issues
│   │   └── commits.py   # /commits (bonus)
│   ├── services/
│   │   └── github.py    # All GitHub API calls
│   └── config.py        # Loads env variables
├── .env                 # GitHub token (NOT committed)
├── .env.example         # Template (committed)
├── .gitignore
├── requirements.txt
└── README.md
