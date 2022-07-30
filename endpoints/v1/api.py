from fastapi import APIRouter
from .endpoints import (category_router, product_router,
                        order_item_router, invoice_router,
                        language_router, order_router,
                        bot_user_router, status_router)

api_v1_router = APIRouter(
    prefix="/api/1"
)

api_v1_router.include_router(category_router)
api_v1_router.include_router(product_router)
api_v1_router.include_router(order_item_router)
api_v1_router.include_router(invoice_router)
api_v1_router.include_router(language_router)
api_v1_router.include_router(order_router)
api_v1_router.include_router(bot_user_router)
api_v1_router.include_router(status_router)
