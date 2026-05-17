from fastapi import APIRouter
from sqlalchemy import text

from app.database.database import SessionLocal

router = APIRouter()

@router.get("/db-check")
def check_database():
    try:
        db = SessionLocal()

        db.execute(text("SELECT 1"))

        return {
            "status": "success",
            "message": "Database connection successful"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        db.close()