from controllers.newsoutlet_controller import router as helloworld_router
from fastapi import FastAPI
import uvicorn
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.getLogger('uvicorn.access').setLevel(logging.INFO)
app.include_router(helloworld_router)

if __name__ == "__main__":
    uvicorn.run("main:app",
    host="127.0.0.1",
    port=5444,
    ssl_certfile="cert.pem",
    ssl_keyfile="key.pem",
    reload=True)