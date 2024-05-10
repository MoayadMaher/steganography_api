from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import *

router = APIRouter()

class HideTextRequest(BaseModel):
    image_url: str
    text: str

@router.post("/hide_text/")
async def hide_text_route_handler(request: HideTextRequest):
    try:
        response = await hide_text(request.image_url, request.text)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ExtractTextRequest(BaseModel):
    image_url: str

@router.post("/extract_text/")
async def extract_text_route_handler(request: ExtractTextRequest):
    try:
        response = await extract_text(request.image_url)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))