from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from supervisor import Supervisor

import shutil
import os

app = FastAPI(
    title="Enterprise HR Copilot API"
)

# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# Supervisor Agent
# ==========================================

supervisor = Supervisor()

# ==========================================
# Health
# ==========================================

@app.get("/health")
def health():

    return {
        "status": "ok",
        "service": "enterprise-hr-copilot"
    }

# ==========================================
# Agents
# ==========================================

@app.get("/agents")
def agents():

    return {
        "agents": [
            "Supervisor Agent",
            "Policy Retrieval Agent",
            "HR Tool Agent",
            "Response Agent"
        ]
    }

# ==========================================
# Chat Endpoint
# ==========================================

@app.post("/chat")
async def chat(payload: dict):

    question = payload.get(
        "message",
        ""
    )

    result = supervisor.run(
        question
    )

    return result

# ==========================================
# Streaming Endpoint
# ==========================================

@app.post("/stream")
async def stream_chat(payload: dict):

    question = payload.get(
        "message",
        ""
    )

    result = supervisor.run(
        question
    )

    answer = result["answer"]

    async def generate():

        words = answer.split()

        for word in words:
            yield word + " "

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )

# ==========================================
# Upload Endpoint
# ==========================================

@app.post("/upload")
async def upload_pdf(
        file: UploadFile = File(...)
):

    try:

        os.makedirs(
            "data",
            exist_ok=True
        )

        file_path = os.path.join(
            "data",
            file.filename
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        return {
            "status": "success",
            "message":
                f"{file.filename} uploaded successfully",
            "path": file_path
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }