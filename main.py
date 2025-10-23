from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
from datetime import datetime, timezone
import logging

from models import ProfileResponse, UserInfo, CatFactResponse
from config import get_settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
settings = get_settings()
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="A RESTful API that returns profile information with dynamic cat facts"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def fetch_cat_fact() -> str:
    """
    Fetch a random cat fact from the Cat Facts API.
    
    Returns:
        str: A random cat fact
        
    Raises:
        HTTPException: If the external API fails
    """
    try:
        async with httpx.AsyncClient() as client:
            logger.info(f"Fetching cat fact from {settings.cat_facts_api_url}")
            response = await client.get(
                settings.cat_facts_api_url,
                timeout=settings.api_timeout
            )
            response.raise_for_status()
            
            data = response.json()
            cat_fact_data = CatFactResponse(**data)
            logger.info(f"Successfully fetched cat fact: {cat_fact_data.fact[:50]}...")
            return cat_fact_data.fact
            
    except httpx.TimeoutException:
        logger.error("Timeout while fetching cat fact")
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="External API timeout - please try again"
        )
    except httpx.HTTPError as e:
        logger.error(f"HTTP error while fetching cat fact: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="External API is currently unavailable"
        )
    except Exception as e:
        logger.error(f"Unexpected error while fetching cat fact: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to the Dynamic Profile Endpoint API",
        "version": settings.app_version,
        "endpoints": {
            "/me": "GET - Fetch profile with dynamic cat fact",
            "/docs": "GET - Interactive API documentation",
            "/health": "GET - Health check endpoint"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get(
    "/me",
    response_model=ProfileResponse,
    responses={
        200: {
            "description": "Successfully retrieved profile with cat fact",
            "content": {
                "application/json": {
                    "example": {
                        "status": "success",
                        "user": {
                            "email": "john.doe@example.com",
                            "name": "John Doe",
                            "stack": "Python/FastAPI"
                        },
                        "timestamp": "2025-10-23T12:34:56.789Z",
                        "fact": "Cats sleep 70% of their lives."
                    }
                }
            }
        },
        503: {"description": "External API unavailable"},
        504: {"description": "External API timeout"}
    }
)
async def get_profile():
    """
    Get profile information with a dynamic cat fact.
    
    Returns a JSON response containing:
    - status: Always "success"
    - user: Object with email, name, and stack
    - timestamp: Current UTC time in ISO 8601 format
    - fact: Random cat fact from Cat Facts API
    
    The endpoint fetches a fresh cat fact on every request.
    """
    try:
        # Fetch cat fact from external API
        cat_fact = await fetch_cat_fact()
        
        # Get current UTC timestamp in ISO 8601 format
        current_timestamp = datetime.now(timezone.utc).isoformat()
        
        # Build response
        response = ProfileResponse(
            status="success",
            user=UserInfo(
                email=settings.user_email,
                name=settings.user_name,
                stack=settings.user_stack
            ),
            timestamp=current_timestamp,
            fact=cat_fact
        )
        
        logger.info(f"Successfully generated profile response at {current_timestamp}")
        
        return JSONResponse(
            content=response.model_dump(),
            media_type="application/json"
        )
        
    except HTTPException:
        # Re-raise HTTP exceptions (already logged in fetch_cat_fact)
        raise
    except Exception as e:
        logger.error(f"Unexpected error in get_profile: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while processing your request"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

