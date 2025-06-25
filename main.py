import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run("src.app:app", host=HOST, port=PORT, reload=True, workers=1)
