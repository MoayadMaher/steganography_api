import subprocess
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from routes import router
from utils import upload_to_cloudinary

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],)

@app.get("/")
def read_root():
    return RedirectResponse(url='/docs')

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)