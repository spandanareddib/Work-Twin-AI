from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException

from app.services.resume_parser.pdf_extractor import extract_text_from_pdf
from app.services.resume_parser.skill_extractor import extract_skills
from app.services.resume_parser.profile_parser import build_profile

app = FastAPI(
    title="WorkTwin AI",
    description="AI-powered Digital Workforce Twin for Career Intelligence",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to WorkTwin AI"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "WorkTwin AI"
    }


@app.post("/resume/upload")
async def upload_resume(file: UploadFile = File(...)):

    # Check that a file was actually selected
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected"
        )

    # Only accept PDF files
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    # Create the resume storage directory
    upload_directory = Path("../data/resumes")
    upload_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    # Create the file path
    file_path = upload_directory / file.filename

    # Read and save the uploaded PDF
    contents = await file.read()

    with open(file_path, "wb") as buffer:
        buffer.write(contents)

    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(str(file_path))

    profile = build_profile(extracted_text)

    return {
    "filename": file.filename,
    "message": "Resume analyzed successfully",
    "profile": profile,
    "text": extracted_text
    }