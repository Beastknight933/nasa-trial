from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import search, recommend

app = FastAPI(title="BioVerse API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search.router)
app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message": "BioVerse API is running 🚀"}


