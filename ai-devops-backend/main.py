from fastapi import FastAPI
from pydantic import BaseModel
import ollama
import requests
from dotenv import load_dotenv
import os
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# FastAPI app
app = FastAPI()

# Request body model
class LogInput(BaseModel):
    logs: str

# Home route
@app.get("/")
def home():
    return {"message": "LLM DevOps Assistant Running"}

# Analyze logs route
@app.post("/analyze")
def analyze_logs(data: LogInput):

    prompt = f"""
    You are an expert DevOps engineer.

    Analyze the following CI/CD pipeline logs carefully.

    Return the response ONLY in this exact format:

    Error:
    <short error>

    Root Cause:
    <why the issue happened>

    Fix:
    <steps to fix the issue>

    CI/CD Logs:
    {data.logs}
    """

    response = ollama.chat(
        model='tinyllama',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return {
        "analysis": response['message']['content']
    }
    
@app.get("/fetch-and-analyze")
def fetch_and_analyze():

    repo_owner = "Scourge4tw"
    repo_name = "ai-devops-demo"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    runs_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs"

    runs_response = requests.get(runs_url, headers=headers)

    runs_data = runs_response.json()

    workflow_runs = runs_data.get("workflow_runs", [])

    if not workflow_runs:
        return {"error": "No workflow runs found"}

    latest_run = workflow_runs[0]

    run_id = latest_run["id"]

    logs_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs/{run_id}/logs"

    logs_response = requests.get(logs_url, headers=headers)

    logs_text = logs_response.text[:4000]

    prompt = f"""
    You are an expert DevOps engineer.

    Analyze these GitHub Actions CI/CD logs.

    Return ONLY in this format:

    Error:
    Root Cause:
    Fix:

    Logs:
    {logs_text}
    """

    response = ollama.chat(
        model="tinyllama",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "run_id": run_id,
        "analysis": response["message"]["content"]
    }
@app.post("/github-webhook")
async def github_webhook(payload: dict):

    print("Webhook received!")

    action = payload.get("action")

    workflow_run = payload.get("workflow_run", {})

    conclusion = workflow_run.get("conclusion")

    if conclusion == "failure":
        print("CI/CD pipeline failed!")

    return {
        "status": "received",
        "conclusion": conclusion
    }