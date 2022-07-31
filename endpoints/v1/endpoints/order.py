from fastapi import APIRouter, HTTPException, Request, Depends

from endpoints.auth.auth_helper import AuthHelper
from schemas import OrderSchema, OrderInDBSchema
from crud import OrderCRUD


order_router = APIRouter(
    prefix="/order",
    tags=["Order"]
)


@order_router.post("/add", status_code=201)
async def add_order(order: OrderSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        order = await OrderCRUD.add(order=order)
        if order:
            return order.id
        raise HTTPException(status_code=409, detail="order is already exists")
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@order_router.get("/get", response_model=OrderInDBSchema)
async def get_order(order_id: int):
    order = await OrderCRUD.get(order_id=order_id)
    if order:
        return order
    raise HTTPException(status_code=404, detail="order not found")


@order_router.get("/all", response_model=list[OrderInDBSchema])
async def get_all_orders():
    orders = await OrderCRUD.get_all()
    if orders:
        return orders
    raise HTTPException(status_code=404, detail="orders not found")


@order_router.put("/update", status_code=200)
async def update_order(order: OrderInDBSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        existing_order = await OrderCRUD.get(order_id=order.id)
        if not existing_order:
            raise HTTPException(status_code=404, detail="order not found")
        await OrderCRUD.update(order=order)
        return order
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@order_router.delete("/del", status_code=204)
async def delete_order(order_id: int, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        order = await OrderCRUD.get(order_id=order_id)
        if not order:
            raise HTTPException(status_code=404, detail="order not found")
        await OrderCRUD.delete(order_id=order_id)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
