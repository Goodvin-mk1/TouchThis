from pydantic import BaseModel


class Categories(BaseModel):
    id: int
    parent_id: int
    is_published: bool
    name_en: str
    name: str


class Products(Categories):
    id: int
    category_id: int
    price: int
    media: str
    total: int
    is_published: bool
    name_en: str
    name: str


class Languages(BaseModel):
    id: int
    language_code: str


class BotUsers(Languages):
    id: int
    is_blocked: bool
    balance: int
    language_id: int


class Statuses(BaseModel):
    id: int
    name: str


class Invoices(BotUsers, Statuses):
    id: int
    bot_user_id: str
    date_create: int
    total: int
    status_id: int


class Orders(Statuses, Invoices, BotUsers):
    id: int
    bot_user_id: str
    date_create: int
    status_id: int
    invoice_id: str


class OrderItems(Products, Orders):
    id: int
    order_id: int
    product_id: int
    total: int
