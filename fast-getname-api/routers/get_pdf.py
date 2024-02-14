from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from werkzeug.utils import secure_filename
from datetime import datetime
import shutil
import os


router = APIRouter()

# Create a temporary directory if it doesn't exist
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# File size limit (5 MB)
MAX_FILE_SIZE = 5 * 1024 * 1024


@router.post("/api/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Ensure that the file is a PDF
        if not file.filename.lower().endswith(".pdf"):
            return JSONResponse(
                status_code=400,
                content={"error": "Only PDF files are allowed"}
            )

        # Check file size
        file.file.seek(0, os.SEEK_END)
        file_size = file.file.tell()
        file.file.seek(0)

        if file_size > MAX_FILE_SIZE:
            return JSONResponse(
                status_code=413,
                content={"error": "File size exceeds the 5MB limit"}
            )

        # Sanitize file name
        safe_filename = secure_filename(file.filename)

        # Check if file exists
        file_path = os.path.join(UPLOAD_DIR, safe_filename)
        if os.path.exists(file_path):
            return JSONResponse(
                status_code=409, content={"error": "File already exists"}
            )

        # Save the uploaded file to the temporary directory
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return (
            {
                "filename": file.filename,
                "message": "File uploaded successfully"
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"error": str(e)}
        )


@router.get("/api/get_pdf/{filename}")
async def get_pdf(filename: str):
    try:
        # Ensure the requested file exists in the upload directory
        file_path = os.path.join(UPLOAD_DIR, filename)
        if not os.path.exists(file_path):
            return JSONResponse(
                status_code=404, content={"error": "File not found"}
            )

        # Return the file using FileResponse
        return FileResponse(
            file_path, media_type="application/pdf", filename=filename
        )
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"error": str(e)}
        )


@router.get("/api/list_pdfs/")
async def get_pdflist():
    try:
        # Get list of filenames in the "uploads" directory
        pdf_details = []
        for filename in os.listdir(UPLOAD_DIR):
            file_path = os.path.join(UPLOAD_DIR, filename)
            creation_at = datetime.fromtimestamp(
                os.path.getctime(file_path)
            )
            pdf_details.append(
                {
                    "filename": filename,
                    "creation_at": creation_at
                }
            )
        return {"pdf_details": pdf_details}
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"error": str(e)}
        )
