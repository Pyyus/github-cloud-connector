from fastapi import APIRouter, HTTPException # type: ignore
from app.services.github import get_repos

router = APIRouter()

@router.get("/repos/{username}")
def fetch_repos(username: str):
    try:
        return get_repos(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))