from fastapi import APIRouter
from .endpoints import category_router, product_router

api_v1_router = APIRouter(
    prefix="/api/1"
)

api_v1_router.include_router(category_router)
api_v1_router.include_router(product_router)
