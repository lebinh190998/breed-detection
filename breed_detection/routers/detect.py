from fastapi import APIRouter, FastAPI

router = APIRouter(
    prefix="/detect",
    tags=["detect"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_detect():
    return "Hello World"


def init_app(app: FastAPI):
    app.include_router(router)