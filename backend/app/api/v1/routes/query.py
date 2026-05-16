from fastapi import APIRouter

router = APIRouter()

@router.get("/query")
def query_test():
    return {
        "message": "Query Route Working Successfully"
    }