from fastapi import APIRouter, FastAPI, UploadFile, File
from ..services.detect import predict
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/detect",
    tags=["detect"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def detect_breed(image: UploadFile = File(...)):
    try:
        breed = await predict(image)
        return JSONResponse(content={"breed": breed})
    
    except FileNotFoundError:
        return JSONResponse(content={"error": "Pkl file not found"}, status_code=404)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

def init_app(app: FastAPI):
    app.include_router(router)