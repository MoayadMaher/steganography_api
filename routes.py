from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import *

router = APIRouter()

class HideTextRequest(BaseModel):
    image_url: str
    text: str

# @router.post("/hide_text/")
# async def hide_text(request: HideTextRequest):
#     try:
#         response = await hide_text(request.image_url, request.text)
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))  

@router.post("/hide_text/")
async def hide_text_route_handler(request: HideTextRequest):
    try:
        response = await hide_text(request.image_url, request.text)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))