from fastapi import APIRouter, HTTPException

from schemas import ProductSchema, ProductInDBSchema
from crud import ProductCRUD


product_router = APIRouter(
    prefix="/product",
    tags=["Products"]
)


@product_router.post("/add", status_code=201)
async def add_product(product: ProductSchema):
    product = await ProductCRUD.add(product=product)
    if product:
        return product.id
    raise HTTPException(status_code=409, detail="product is already exists")


@product_router.get("/get", response_model=ProductInDBSchema)
async def get_product(product_id: int):
    product = await ProductCRUD.get(product_id=product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="product not found")


@product_router.get("/all", response_model=list[ProductInDBSchema])
async def get_all_products():
    products = await ProductCRUD.get_all()
    if products:
        return products
    raise HTTPException(status_code=404, detail="products not found")


@product_router.put("/update", status_code=200)
async def update_product(product: ProductInDBSchema):
    existing_product = await ProductCRUD.get(product_id=product.id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="product not found")
    await ProductCRUD.update(product=product)
    return product


@product_router.delete("/del", status_code=204)
async def delete_product(product_id: int):
    product = await ProductCRUD.get(product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    await ProductCRUD.delete(product_id=product_id)


