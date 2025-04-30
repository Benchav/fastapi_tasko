from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.task_routes import router as task_router

app = FastAPI(title="API Tasko", version="1.0")

app.include_router(user_router)
app.include_router(task_router)