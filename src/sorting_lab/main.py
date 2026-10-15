from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from sorting_lab.api.routes import router

WEB_DIR = Path(__file__).resolve().parent / "web"

app = FastAPI(
    title="Sorting Lab API",
    description="Laboratório educacional de ordenação de inteiros",
    version="0.1.0",
)

app.include_router(router)

if WEB_DIR.is_dir():
    app.mount("/", StaticFiles(directory=WEB_DIR, html=True), name="web")
