from fastapi import FastAPI

from endpoints.auth.api import auth_router
from endpoints.v1 import api_v1_router


tags = [
    {
        "name": "Category",
        "description": "Endpoints for category"
    },
    {
        "name": "Product",
        "description": "Endpoints for product"
    },
    {
        "name": "Bot User",
        "description": "Endpoints for bot user"
    },
    {
        "name": "Invoice",
        "description": "Endpoints for invoice"
    },
    {
        "name": "Language",
        "description": "Endpoints for language"
    },
    {
        "name": "Order",
        "description": "Endpoints for order"
    },
    {
        "name": "Order Item",
        "description": "Endpoints for order item"
    },
    {
        "name": "Status",
        "description": "Endpoints for status"
    },
    {
        "name": "User",
        "description": "Endpoints for user"
    }
]
app = FastAPI(
    title="Online shop",
    openapi_tags=tags
)
app.include_router(api_v1_router)
app.include_router(auth_router)
