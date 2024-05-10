import cloudinary.uploader
from config import CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET
import cloudinary
import requests
import shutil
import os
from datetime import datetime

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

def upload_to_cloudinary(file_path: str) -> str:
    response = cloudinary.uploader.upload(file_path, folder="stego")
    print("uitls", response)
    return response['secure_url']

def download_image(url: str) -> str:
    local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename

def write_text_to_file(text: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"text_{timestamp}.txt"

    with open(filename, 'w') as file:
        file.write(text)
    print(f"Text written to {filename}")

    return filename

def cleanup_files(file_paths):
    for file_path in file_paths:
        os.remove(file_path)

