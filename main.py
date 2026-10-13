import os
import httpx
from fastapi import FastAPI
# from fastapi import Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:4b")

SYSTEM_PROMPT = (
   "تو یک دستیار پشتیبان و صمیمی برای ارتباط با کاربر هستی. "
    "به زبان فارسی کاملاً روان، خودمانی و کوتاه جواب بده (مثل یک انسان واقعی در چت). "
    "اگر جواب سوالی را نمی‌دانی، خیلی ساده و صمیمی بگو: 'راستش رو بخوای، اطلاعات دقیقی در این مورد ندارم.' "
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def ask_ollama(request: ChatRequest):  
    user_text = request.message
    
    # لاگ 1: چک کردن متغیرها
    print(f"DEBUG: Target URL: {OLLAMA_URL}")
    print(f"DEBUG: Model: {MODEL_NAME}")
    
    ollama_payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ],
        "stream": False,
        "options": {"temperature": 0.7}
    }

    try:
        async with httpx.AsyncClient() as client:
            print("DEBUG: Sending request to Ollama...")
            
            response = await client.post(OLLAMA_URL, json=ollama_payload, timeout=60.0)
            
            print(f"DEBUG: Response Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print("DEBUG: Raw Data Received:", data) 
                
                bot_reply = data.get("message", {}).get("content", "پاسخی در فیلد content نبود")
                return {"status": "success", "reply": bot_reply}
            else:
                error_msg = f"Ollama returned error: {response.text}"
                print(f"DEBUG: {error_msg}")
                return {"status": "error", "detail": error_msg}

    except Exception as e:
        print(f"DEBUG: CRITICAL ERROR: {str(e)}")
        return {"status": "error", "detail": str(e)}


@app.get("/")
async def root():
    return {"status": "running"}


"""
@app.get("/webhook")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == "MY_VERIFY_TOKEN":
        return int(challenge)
    return "Forbidden", 403

@app.post("/webhook")
async def handle_instagram_webhook(payload: dict):
    entry = payload.get("entry", [{}])[0]
    messaging = entry.get("messaging", [{}])[0]
    sender_id = messaging.get("sender", {}).get("id")
    user_text = messaging.get("message", {}).get("text")

    if user_text:
        bot_reply = await ask_ollama(user_text)
        
        await send_to_instagram_api(sender_id, bot_reply)
        
    return {"status": "ok"}

"""