from fastapi import APIRouter, FastAPI, UploadFile
from ..services.detect import predict
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/detect",
    tags=["detect"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def detect_breed(image: UploadFile):
    breed = await predict(image)
    return JSONResponse(content={"breed": breed})

def init_app(app: FastAPI):
    app.include_router(router)