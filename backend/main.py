from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers.users import router as users_router
from backend.routers.rubrics import router as rubrics_router
from backend.routers.exams import router as exams_router
from backend.routers.temp_exams import router as temp_exams_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(rubrics_router)
app.include_router(exams_router)
app.include_router(temp_exams_router)


