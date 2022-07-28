from fastapi import FastAPI

from endpoints.v1 import api_v1_router

app = FastAPI(
    title="Online shop",
)
app.include_router(api_v1_router)

