import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_BASE_URL = "https://api.github.com"