from fastapi import APIRouter, HTTPException, Depends
from backend.auth import get_current_user
from backend.repo.exam_repo import (
    get_all_user_exams,
    get_exam,
    save_exam_correction,
    update_exam,
)
from backend.repo.temp_exams_repo import get_temp_exam
from fastapi.responses import StreamingResponse
import io

router = APIRouter(prefix="/exams", tags=["Exams"])


def _get_owned_exam(exam_id: str, user: dict):
    exam = get_exam(exam_id)
    if not exam or str(exam.get("user_id")) != user["id"]:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam


@router.get("/all_my_exams")
async def get_user_full_exams(user: dict = Depends(get_current_user)):
    try:
        all_exams = get_all_user_exams(user["id"])
        return {"exams": all_exams}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{exam_id}")
async def get_exam_endpoint(exam_id: str, user: dict = Depends(get_current_user)):
    return _get_owned_exam(exam_id, user)


@router.put("/{exam_id}")
async def update_exam_endpoint(exam_id: str, updated_data: dict, user: dict = Depends(get_current_user)):
    _get_owned_exam(exam_id, user)
    updated_data.pop("user_id", None)
    try:
        updated_exam = update_exam(exam_id, updated_data)
        return {
            "message": "Exam updated successfully",
            "exam": updated_exam
        }
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/finalize-correction/{temp_exam_id}")
async def save_exam_endpoint(temp_exam_id: str, user: dict = Depends(get_current_user)):
    try:
        temp_exam = get_temp_exam(temp_exam_id)
    except Exception:
        temp_exam = None
    if not temp_exam or str(temp_exam.get("user_id")) != user["id"]:
        raise HTTPException(status_code=404, detail="Temporary exam not found")

    try:
        new_id = save_exam_correction(temp_exam_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "message": "Correction confirmed and moved to final collection",
        "exam_id": new_id,
    }


@router.get("/download-report/{exam_id}")
async def download_report(exam_id: str, user: dict = Depends(get_current_user)):
    exam = _get_owned_exam(exam_id, user)

    from backend.orchestrator import generate_pdf_report

    pdf_bytes = generate_pdf_report(exam)

    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename=Exam_Report_{exam_id}.pdf"}
    )
