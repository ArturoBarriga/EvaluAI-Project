from fastapi import APIRouter, HTTPException, Depends
from backend.auth import get_current_user
from backend.repo.rubric_repo import (
    create_rubric,
    get_rubrics,
    update_rubric,
    delete_rubric,
    get_rubric_by_id,
)

router = APIRouter(prefix="/rubrics", tags=["Rubrics"])


def _get_owned_rubric(rubric_id: str, user: dict):
    try:
        rubric = get_rubric_by_id(rubric_id)
    except Exception:
        rubric = None
    if not rubric or rubric.get("creator") != user["email"]:
        raise HTTPException(status_code=404, detail="Rubric not found")
    return rubric


@router.post("/create")
async def create_rubric_endpoint(rubric: dict, user: dict = Depends(get_current_user)):
    rubric["creator"] = user["email"]
    if not rubric.get("name") or not rubric.get("questions"):
        raise HTTPException(status_code=400, detail="Missing required fields")

    for question in rubric["questions"]:
        if "text" not in question or not question["text"]:
            raise HTTPException(status_code=400, detail="Missing text in one of the questions")
        if "criteria" not in question or not question["criteria"]:
            raise HTTPException(status_code=400, detail="Missing criteria in one of the questions")

        for criterion in question["criteria"]:
            if not all(k in criterion for k in ("description", "points")):
                raise HTTPException(status_code=400, detail="Invalid criterion format in one of the questions")

    rubric_id = create_rubric(rubric)

    return {"message": "Rubric created successfully", "id": rubric_id}


@router.get("/mine")
async def get_rubrics_endpoint(user: dict = Depends(get_current_user)):
    return get_rubrics(user["email"])


@router.get("/get/{rubric_id}")
async def get_rubric_by_id_endpoint(rubric_id: str, user: dict = Depends(get_current_user)):
    return _get_owned_rubric(rubric_id, user)


@router.put("/{rubric_id}")
async def update_rubric_endpoint(rubric_id: str, new_data: dict, user: dict = Depends(get_current_user)):
    _get_owned_rubric(rubric_id, user)
    new_data.pop("creator", None)
    if update_rubric(rubric_id, new_data):
        return {"message": "Rubric updated"}
    else:
        raise HTTPException(status_code=404, detail="Rubric not found")


@router.delete("/{rubric_id}")
async def delete_rubric_endpoint(rubric_id: str, user: dict = Depends(get_current_user)):
    _get_owned_rubric(rubric_id, user)
    if delete_rubric(rubric_id):
        return {"message": "Rubric deleted"}
    else:
        raise HTTPException(status_code=404, detail="Rubric not found")
