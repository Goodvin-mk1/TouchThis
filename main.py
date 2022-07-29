from fastapi import FastAPI

from endpoints.v1 import api_v1_router


tags = [
    {
        "name": "Categories",
        "description": "Endpoints for categories"
    },
    {
        "name": "Products",
        "description": "Endpoints for products"
    }

]
app = FastAPI(
    title="Online shop",
    openapi_tags=tags
)
app.include_router(api_v1_router)

