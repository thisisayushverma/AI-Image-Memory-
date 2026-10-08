from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.tasks.tasks import process_image
import os
import shutil
import uuid


app = FastAPI(
    title="AI Image Memory API",
    description="Backend for AI Image Memory",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "AI Image Memory API is running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.post("/upload-images")
async def uploadImage(images:list[UploadFile] = File(...)):
    try:
        print(f"images data {images}")
        upload_dir = "uploads"

        # Create folder if it doesn't exist
        os.makedirs(upload_dir, exist_ok=True)

        for image in images:
            imgId = str(uuid.uuid4())
            print(f"image id - {imgId}")
            file_path = os.path.join(upload_dir, imgId)

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            process_image.delay(imgId)
        

        return {
                "data":"Images Upload successfully",
                "success": True
            }
    except Exception as e:
        return {
            "success":False,
            "error":str(e)
        }
    