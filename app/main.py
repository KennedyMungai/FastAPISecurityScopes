"""The main app for the application"""
from fastapi import FastAPI


app = FastAPI(
    title="Security Scopes",
    description="A simple security scopes experiment",
    version="0.1.0"
)


@app.get("/")
async def root() -> dict[str, str]:
    """The root endpoint of the application

    Returns:
        dict[str, str]: A simple message
    """
    return {"message": "Hello World"}
