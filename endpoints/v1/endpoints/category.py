from fastapi import APIRouter, HTTPException

from schemas import CategorySchema, CategoryInDBSchema, CategoryInDBSchemaExtended, ProductInDBSchema
from crud import CategoryCRUD


category_router = APIRouter(
    prefix="/category",
    tags=["Categories"]
)


@category_router.post("/add", status_code=201)
async def add_category(category: CategorySchema):
    category = await CategoryCRUD.add(category=category)
    if category:
        return category.id
    raise HTTPException(status_code=409, detail="category is already exists")


@category_router.get("/get", response_model=CategoryInDBSchema)
async def get_category(category_id: int):
    category = await CategoryCRUD.get(category_id=category_id)
    if category:
        return category
    raise HTTPException(status_code=404, detail="category not found")


@category_router.get("/all", response_model=list[CategoryInDBSchemaExtended])
async def get_all_categories(parent_id: int = None):
    categories = await CategoryCRUD.get_all(parent_id=parent_id)
    if parent_id is None:
        tree_view_categories = await get_tree_view_categories(categories)
        if tree_view_categories:
            return tree_view_categories
    else:
        if categories:
            return categories
    raise HTTPException(status_code=404, detail="categories not found")


async def get_tree_view_categories(categories: list[CategoryInDBSchema]) -> list[CategoryInDBSchemaExtended]:
    extended_categories = [CategoryInDBSchemaExtended(**category.__dict__) for category in categories]

    base_categories = [extended_categories.pop(extended_categories.index(category))
                       for category in extended_categories if category.parent_id is None]

    for category in extended_categories:
        if category.parent_id is not None:
            await find_child(base_categories, category)

    return base_categories


async def find_child(base_categories: list[CategoryInDBSchemaExtended], child_category: CategoryInDBSchemaExtended):
    for base_category in base_categories:
        if base_category.id == child_category.parent_id:
            base_category.child_categories.append(child_category)
        elif base_category.child_categories:
            await find_child(base_category.child_categories, child_category)


@category_router.get("/get/products", response_model=list[tuple[CategoryInDBSchema, ProductInDBSchema]])
async def get_products_by_category_id(category_id: int):
    print(category_id)
    category_with_products = await CategoryCRUD.get_products_by_category_id(category_id=category_id)
    print(category_with_products)

    if category_with_products:
        return category_with_products
    raise HTTPException(status_code=404, detail="category not found")


@category_router.put("/update", status_code=200)
async def update_category(category: CategoryInDBSchema):
    existing_category = await CategoryCRUD.get(category_id=category.id)
    if not existing_category:
        raise HTTPException(status_code=404, detail="category not found")
    await CategoryCRUD.update(category=category)
    return category


@category_router.delete("/del", status_code=204)
async def delete_category(category_id: int):
    category = await CategoryCRUD.get(category_id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="category not found")
    await CategoryCRUD.delete(category_id=category_id)


