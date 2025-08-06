from fastapi import FastAPI
from src.api.router import router as api_router
import uvicorn
app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)