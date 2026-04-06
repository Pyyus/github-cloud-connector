from fastapi import APIRouter, HTTPException # type: ignore
from pydantic import BaseModel        # type: ignore
from app.services.github import list_issues, create_issue

router = APIRouter()

class IssueRequest(BaseModel):
    owner: str
    repo: str
    title: str
    body: str = ""

@router.get("/list-issues/{owner}/{repo}")
def get_issues(owner: str, repo: str):
    try:
        return list_issues(owner, repo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/create-issue")
def new_issue(issue: IssueRequest):
    try:
        return create_issue(issue.owner, issue.repo, issue.title, issue.body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))