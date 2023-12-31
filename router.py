from fastapi import APIRouter, FastAPI, UploadFile
from service import predict
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/detect",
    tags=["detect"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_breed():
    return JSONResponse(content={"breed": "YES"})

@router.post("/")
async def detect_breed(image: UploadFile):
    try:
        print("---- BEFORE ENDPOINT ----")
        is_cat = await predict(image)
        
        if is_cat == True:
            return JSONResponse(content={"breed": "Cat"})
        else:
            return JSONResponse(content={"breed": "Dog"})
            
    
    except FileNotFoundError:
        return JSONResponse(content={"error": "Pkl file not found"}, status_code=404)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

def init_app(app: FastAPI):
    app.include_router(router)