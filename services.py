import subprocess
from utils import *

async def hide_text(image_url: str, text: str) -> dict:
    try :
        image_path = download_image(image_url)
        text_file_path = write_text_to_file(text)
        stego_image_path = f"stego_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        command = [
            "python3", "stego.py", "-e", "-i",
            image_path, "-f", text_file_path, "-o", stego_image_path
        ]
        subprocess.run(command, check=True )
        
        cloudinary_url = upload_to_cloudinary(stego_image_path)
        cleanup_files([image_path, text_file_path, stego_image_path])

    except Exception as e:
        cleanup_files([image_path, text_file_path, stego_image_path])
        raise e

    return {"stego_image_url": cloudinary_url}

async def extract_text(image_url: str) -> dict:
    try:
        image_path = download_image(image_url)
        text_file_path = f"extracted_text_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        command =[ "python3", "stego.py", "-d", "-i", image_path, "-f", text_file_path]
        subprocess.run(command, check=True)

        with open(text_file_path, "r") as f:
            extracted_text = f.read()
        
        cleanup_files([image_path, text_file_path])
    except Exception as e:
        cleanup_files([image_path, text_file_path])
        raise e
    return {"extract_text": extracted_text}

        
        

    
