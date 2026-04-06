from fastapi import FastAPI   # type: ignore
from app.routes import repos, issues

app = FastAPI(title="GitHub Cloud Connector", version="1.0.0")

app.include_router(repos.router)
app.include_router(issues.router)

@app.get("/")
def root():
    return {"message": "GitHub Connector is running!"}