from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import detect
import pkgutil
import importlib
import os
import inspect

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def app_init() -> FastAPI:
    app = FastAPI()
    
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
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
        if hasattr(module, "router"):
            app.include_router(module.router)
    

# def load_modules(app: FastAPI = None) -> None:
#     for ep in entry_points()["breed_detection.modules"]:
#         print("Loading module: %s", ep.name)
#         mod = ep.load()
#         if app:
#             init_app = getattr(mod, "init_app", None)
#             if init_app:
#                 init_app(app)
