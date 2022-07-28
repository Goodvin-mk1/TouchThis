from fastapi import APIRouter, HTTPException

from schemas import CategorySchema, CategoryInDBSchema, CategoryInDBSchemaExtended
from crud import CategoryCRUD


category_router = APIRouter(
    prefix="/category"
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
    extended_categories = [CategoryInDBSchemaExtended(**category.__dict__) for category in categories]
    tree_categories = await get_root_categories(extended_categories)
    if tree_categories:
        return tree_categories
    raise HTTPException(status_code=404, detail="categories not found")


async def get_root_categories(extended_categories: list[CategoryInDBSchemaExtended]) -> list[CategoryInDBSchemaExtended]:
    for category in extended_categories:
        if category.parent_id is not None:
            await find_child(extended_categories, category.parent_id)

    return extended_categories


async def find_child(categories: list[CategoryInDBSchemaExtended], parent_id: int):
    for category in categories:
        if category.id == parent_id:
            sub_categories = [sub for sub in categories if sub.parent_id == parent_id]
            if len(sub_categories) != 0:
                for sub_category in sub_categories:
                    await find_child(sub_categories, sub_category.parent_id)
                    #if sub_category.parent_id is None:
                    #categories.remove(sub_category)
            category.sub_categories.append(sub_categories)
            for sub_category in category.sub_categories:
                for cat in categories:
                    if cat.parent_id == sub_category.parent_id:
                        categories.remove(cat)


@category_router.get("/get/products", response_model=list[CategoryInDBSchema])
async def get_products_by_category_id(category_id: int):
    category_with_products = await CategoryCRUD.get_products_by_category_id(category_id=category_id)
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


