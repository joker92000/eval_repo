import logging
import httpx  # Ajoutez cette ligne
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mini_groq import call_groq_api

app = FastAPI()
logging.basicConfig(level=logging.INFO)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/status")
async def get_status():
    return {"status": "ok"}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        logging.info(f"Received prompt: {request.prompt}")
        response = await call_groq_api(request.prompt)
        logging.info(f"Response from Groq API: {response}")
        return response
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error: {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
