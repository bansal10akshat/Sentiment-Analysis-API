from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import analyze_sentiment

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze(request: TextRequest):
    try:
        result = analyze_sentiment(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))