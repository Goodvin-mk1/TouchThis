from fastapi import APIRouter, HTTPException, Request, Depends

from endpoints.auth.user_validate import AuthHelper
from schemas import StatusSchema, StatusInDBSchema
from crud import StatusCRUD


status_router = APIRouter(
    prefix="/status",
    tags=["Status"]
)


@status_router.post("/add", status_code=201)
async def add_status(status: StatusSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        status = await StatusCRUD.add(status=status)
        if status:
            return status.id
        raise HTTPException(status_code=409, detail="status is already exists")
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@status_router.get("/get", response_model=StatusInDBSchema)
async def get_status(status_id: int):
    status = await StatusCRUD.get(status_id=status_id)
    if status:
        return status
    raise HTTPException(status_code=404, detail="status not found")


@status_router.get("/all", response_model=list[StatusInDBSchema])
async def get_all_statuses():
    statuses = await StatusCRUD.get_all()
    if statuses:
        return statuses
    raise HTTPException(status_code=404, detail="status not found")


@status_router.put("/update", status_code=200)
async def update_status(status: StatusInDBSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        existing_status = await StatusCRUD.get(status_id=status.id)
        if not existing_status:
            raise HTTPException(status_code=404, detail="status not found")
        await StatusCRUD.update(status=status)
        return status
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@status_router.delete("/del", status_code=204)
async def delete_status(status_id: int, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        status = await StatusCRUD.get(status_id=status_id)
        if not status:
            raise HTTPException(status_code=404, detail="status not found")
        await StatusCRUD.delete(status_id=status_id)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
