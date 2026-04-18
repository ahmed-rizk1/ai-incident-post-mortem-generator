from fastapi import FastAPI
from src.routes.incident import router as incident_router
from fastapi.middleware.cors import CORSMiddleware
from src.helpers.config import config

app = FastAPI(title="AI Incident Post-Mortem API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(incident_router)

def main():
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=config.API_PORT, reload=True)

if __name__ == "__main__":
    main()
