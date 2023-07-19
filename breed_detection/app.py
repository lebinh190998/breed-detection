from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pkgutil
import importlib
import os
import inspect
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def app_init() -> FastAPI:
    app = FastAPI()
    
    origins = ["https://visionpaws.vercel.app", "http://localhost", "http://localhost:3000"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["Content-Disposition"],
        max_age=600,
    )
    
    load_modules(app)

    return app

def load_modules(app: FastAPI = None) -> None:
    current_file = inspect.getfile(inspect.currentframe())
    package_name = os.path.basename(os.path.dirname(current_file))
    package_path = os.path.join(package_name, "routers")

    # Discover and include routers dynamically
    for _, module_name, _ in pkgutil.iter_modules([package_path]):
        module = importlib.import_module(f"{package_name}.routers.{module_name}")
        init_app = getattr(module, "init_app", None)
        if init_app:
            init_app(app)
