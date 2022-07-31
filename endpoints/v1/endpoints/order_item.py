from fastapi import APIRouter, HTTPException, Request, Depends

from endpoints.auth.user_validate import AuthHelper
from schemas import OrderItemSchema, OrderItemInDBSchema
from crud import OrderItemCRUD


order_item_router = APIRouter(
    prefix="/order_item",
    tags=["Order Item"]
)


@order_item_router.post("/add", status_code=201)
async def add_order_item(order_item: OrderItemSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        order_item = await OrderItemCRUD.add(order_item=order_item)
        if order_item:
            return order_item.id
        raise HTTPException(status_code=409, detail="order item is already exists")
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@order_item_router.get("/get", response_model=OrderItemInDBSchema)
async def get_order_item(order_item_id: int):
    order_item = await OrderItemCRUD.get(order_item_id=order_item_id)
    if order_item:
        return order_item
    raise HTTPException(status_code=404, detail="order item not found")


@order_item_router.get("/all", response_model=list[OrderItemInDBSchema])
async def get_all_order_items():
    order_items = await OrderItemCRUD.get_all()
    if order_items:
        return order_items
    raise HTTPException(status_code=404, detail="order items not found")


@order_item_router.put("/update", status_code=200)
async def update_order_item(order_item: OrderItemInDBSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        existing_order_item = await OrderItemCRUD.get(order_item_id=order_item.id)
        if not existing_order_item:
            raise HTTPException(status_code=404, detail="order item not found")
        await OrderItemCRUD.update(order_item=order_item)
        return order_item
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@order_item_router.delete("/del", status_code=204)
async def delete_order_item(order_item_id: int, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        order_item = await OrderItemCRUD.get(order_item_id=order_item_id)
        if not order_item:
            raise HTTPException(status_code=404, detail="order item not found")
        await OrderItemCRUD.delete(order_item_id=order_item_id)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
