import uvicorn
from fastapi import FastAPI

from oauth2flow.routes import oauth_router

app = FastAPI(
    title="oauth2 flow",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(
    oauth_router,
    prefix="/api/v1/oauth",
)


if __name__ == "__main__":
    uvicorn.run(
        "oauth2flow.main:app",
        host="0.0.0.0",
        reload=True,
        port=9000,
    )
