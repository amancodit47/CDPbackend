from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from cdp_support_bot import CDPSupportBot

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-netlify-app.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the bot with sample responses
bot = CDPSupportBot()

class Question(BaseModel):
    text: str
    platform: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "CDP Support Bot API is running"}

@app.post("/ask")
async def ask_question(question: Question):
    try:
        response = bot.answer_question(question.text)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
