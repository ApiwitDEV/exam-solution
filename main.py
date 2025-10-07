from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()


@app.get("/exam_images")
async def root(page: int):
    # Define the path to your image file
    image_path = f"/Users/bas/Downloads/exam_images/page_{page}.png" 
    if not os.path.exists(image_path):
        # Handle case where the file doesn't exist
        return {"message": "Image not found"}, 404
    return FileResponse(image_path, media_type="image/png")