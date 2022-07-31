from fastapi import APIRouter, HTTPException, Request, Depends

from endpoints.auth.auth_helper import AuthHelper
from schemas import InvoiceSchema, InvoiceInDBSchema
from crud import InvoiceCRUD


invoice_router = APIRouter(
    prefix="/invoice",
    tags=["Invoice"]
)


@invoice_router.post("/add", status_code=201)
async def add_invoice(invoice: InvoiceSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        invoice = await InvoiceCRUD.add(invoice=invoice)
        if invoice:
            return invoice.id
        raise HTTPException(status_code=409, detail="invoice is already exists")
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@invoice_router.get("/get", response_model=InvoiceInDBSchema)
async def get_invoice(invoice_id: int):
    invoice = await InvoiceCRUD.get(invoice_id=invoice_id)
    if invoice:
        return invoice
    raise HTTPException(status_code=404, detail="invoice not found")


@invoice_router.get("/all", response_model=list[InvoiceInDBSchema])
async def get_all_invoices():
    invoices = await InvoiceCRUD.get_all()
    if invoices:
        return invoices
    raise HTTPException(status_code=404, detail="invoices not found")


@invoice_router.put("/update", status_code=200)
async def update_invoice(invoice: InvoiceInDBSchema, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        existing_invoice = await InvoiceCRUD.get(invoice_id=invoice.id)
        if not existing_invoice:
            raise HTTPException(status_code=404, detail="invoice not found")
        await InvoiceCRUD.update(invoice=invoice)
        return invoice
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@invoice_router.delete("/del", status_code=204)
async def delete_invoice(invoice_id: int, request: Request = Depends(AuthHelper.validate_user)):
    if request:
        invoice = await InvoiceCRUD.get(invoice_id=invoice_id)
        if not invoice:
            raise HTTPException(status_code=404, detail="invoice not found")
        await InvoiceCRUD.delete(invoice_id=invoice_id)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
