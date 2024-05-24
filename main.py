from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mini_groq import call_groq_api  # Mise à jour de l'importation

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.get("/status")
async def get_status():
    return {"status": "ok"}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = await call_groq_api(request.prompt)
        return response
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
