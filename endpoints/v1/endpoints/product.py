from fastapi import APIRouter, HTTPException, Request, Depends

from endpoints.auth.user_validate import AuthHelper
from schemas import ProductSchema, ProductInDBSchema, CategoryInDBSchema
from crud import ProductCRUD


product_router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@product_router.post("/add", status_code=201)
async def add_product(product: ProductSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        product = await ProductCRUD.add(product=product)
        if product:
            return product.id
        raise HTTPException(status_code=409, detail="product is already exists")
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


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


@product_router.get("/category", response_model=tuple[ProductInDBSchema, CategoryInDBSchema])
async def get_category_of_product(product_id: int):
    category_of_product = await ProductCRUD.get_category_of_product(product_id=product_id)
    if category_of_product:
        return category_of_product
    raise HTTPException(status_code=404, detail="product not found")


@product_router.put("/update", status_code=200)
async def update_product(product: ProductInDBSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        existing_product = await ProductCRUD.get(product_id=product.id)
        if not existing_product:
            raise HTTPException(status_code=404, detail="product not found")
        await ProductCRUD.update(product=product)
        return product
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@product_router.delete("/del", status_code=204)
async def delete_product(product_id: int, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        product = await ProductCRUD.get(product_id=product_id)
        if not product:
            raise HTTPException(status_code=404, detail="product not found")
        await ProductCRUD.delete(product_id=product_id)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
