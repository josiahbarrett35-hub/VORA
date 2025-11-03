from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    title="VORA - Life Operating System",
    description="Timing Intelligence + Emotional Intelligence",
    version="0.1.0",
)

# CORS middleware (allow frontend local dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return JSONResponse({"status": "healthy", "version": "0.1.0"})

@app.get("/")
async def root():
    return {"message": "VORA API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
