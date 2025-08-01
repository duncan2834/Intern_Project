from fastapi import FastAPI
from src.api.router import router as api_router
import uvicorn

app = FastAPI()

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "hello"}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)