from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.image_processing import router as image_router
from app.config.logger import logger
from app.config.settings import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # No database or disk setup: this service is stateless by design.
    # Java owns all storage — see the image endpoints for the contract.
    logger.info(f"Starting {settings.application.name} Service...")
    yield
    logger.info(f"Shutting down {settings.application.name} Service...")

app = FastAPI(
    title=settings.application.name,       
    version=settings.application.version,   
    description=settings.application.description, 
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(image_router, prefix=settings.application.api_prefix)


@app.get("/")
async def root():
    return {
        "message": f"{settings.application.name} is running" 
    }

@app.get("/health")
async def health():
    logger.debug("Health check endpoint hit.")
    return {
        "status": "healthy"
    }

@app.get("/version")
async def version():
    return {
        "version": settings.application.version 
    }