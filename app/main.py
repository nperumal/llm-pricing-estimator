from fastapi import FastAPI
from app.dependencies import authenticate
from app.token_calculations import calculate_text_tokens, calculate_audio_tokens, calculate_image_tokens
from app.models import TextInput
from fastapi import HTTPException, Depends, UploadFile, File, Form
from typing import Optional

app = FastAPI()

@app.post("/text_tokens", dependencies=[Depends(authenticate)])
def text_tokens(input_data: TextInput):
    print(input_data)
    """Endpoint for calculating tokens from text input."""
    token_count = calculate_text_tokens(input_data.text, input_data.model_name)
    return {"tokens": token_count}

@app.post("/audio_tokens", dependencies=[Depends(authenticate)])
def audio_tokens(file: UploadFile = File(...), model_name: Optional[str] = Form(...)):
    """Endpoint for calculating tokens from audio input."""
    return {"error": "Audio token calculation is not supported in this environment."}

@app.post("/image_tokens", dependencies=[Depends(authenticate)])
def image_tokens(file: UploadFile = File(...), model_name: Optional[str] = Form(...)):
    """Endpoint for calculating tokens from image input."""
    return {"error": "Image token calculation is not supported in this environment."}

@app.get("/health", dependencies=[Depends(authenticate)])
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}