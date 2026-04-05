from fastapi import FastAPI
from app.api.routes.auth_routes import router as auth_router
from app.api.routes.admin_routes import router as admin_router

app = FastAPI(title="Auth API")

app.include_router(auth_router, prefix="/auth", tags=["User Authentication"])
app.include_router(admin_router, prefix="/admin", tags=["Admin Actions"])