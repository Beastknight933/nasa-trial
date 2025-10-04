from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import search, recommend, describe

app = FastAPI(
    title="BioVerse API",
    version="1.0",
    description="Backend for NASA BioVerse project 🚀",
)

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict this to frontend origin if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all route modules
app.include_router(search.router)
app.include_router(recommend.router)
app.include_router(describe.router)


@app.get("/")
def root():
    return {
        "message": "BioVerse API is live 🚀",
        "endpoints": ["/search", "/recommend", "/describe"]
    }


