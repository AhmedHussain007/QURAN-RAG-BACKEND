from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.quran import router as quran_router
from .rag.bm25_engine import BM25Search

bm25_engine = BM25Search()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quran_router, prefix="/api/quran", tags=["Quran Search"])
