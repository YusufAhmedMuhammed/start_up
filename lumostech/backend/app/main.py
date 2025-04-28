from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.api.v1.endpoints import contact, leads, admin

app = FastAPI(
    title="SaaS Agency Platform API",
    description="Backend API for the SaaS Agency Platform",
    version="1.0.0",
)

# Security middleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return JSONResponse(
        content={
            "message": "Welcome to the SaaS Agency Platform API",
            "status": "healthy",
        }
    )

# Include routers
app.include_router(contact.router, prefix="/api/v1", tags=["contact"])
app.include_router(leads.router, prefix="/api/v1", tags=["leads"])
app.include_router(admin.router, prefix="/api/v1", tags=["admin"])

# Import and include routers
# from app.api.v1 import router as api_v1_router
# app.include_router(api_v1_router, prefix="/api/v1") 