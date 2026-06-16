from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

from backend.services.dataset_service import load_dataset
from backend.services.chatbot_service import process_question
from backend.services.cleaning_service import export_cleaned_dataset

app = FastAPI()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    load_dataset(file_path)

    return {"message": "Dataset uploaded successfully"}

@app.post("/chat")
async def chat(data: dict):

    question = data["question"]

    response = process_question(question)

    return {"response": response}

@app.get("/download")
def download_dataset():

    file_path = export_cleaned_dataset()

    if file_path is None:
        return {"message": "No dataset uploaded"}

    return FileResponse(
        path=file_path,
        filename="cleaned_dataset.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )