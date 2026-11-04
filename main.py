from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.get("/health")
def healthCheck():
    return Response("Healthy!!!", status_code=200)
