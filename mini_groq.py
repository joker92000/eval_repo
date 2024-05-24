import httpx
import os
from dotenv import load_dotenv
import logging

load_dotenv()

GROQ_API_URL = "https://api.groq.com/v1/endpoint"  # Remplacez par l'URL correcte de l'API Groq
GROQ_API_TOKEN = os.getenv("GROQ_API_TOKEN")

async def call_groq_api(prompt: str):
    headers = {
        "Authorization": f"Bearer {GROQ_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt
    }

    async with httpx.AsyncClient() as client:
        logging.info(f"Sending request to Groq API with prompt: {prompt}")
        response = await client.post(GROQ_API_URL, json=data, headers=headers)
        logging.info(f"Received response: {response.status_code} - {response.text}")
        response.raise_for_status()  # Cela lèvera une exception pour les réponses d'erreur HTTP
        return response.json()
