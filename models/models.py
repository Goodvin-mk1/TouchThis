from datetime import datetime

from sqlalchemy import (Column, SmallInteger,
                        ForeignKey, VARCHAR,
                        CHAR, DECIMAL,
                        TIMESTAMP, Boolean, Integer, Text)
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__: str = "categories"

    id = Column(SmallInteger, primary_key=True)
    parent_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"), default=None)
    is_published = Column(Boolean, default=False)
    name = Column(VARCHAR(20), nullable=False, unique=True)


class Product(Base):
    __tablename__: str = "products"

    id = Column(SmallInteger, primary_key=True)
    category_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    price = Column(DECIMAL(7, 2), nullable=False)
    total = Column(DECIMAL(7, 2))
    is_published = Column(Boolean, default=False)
    name = Column(VARCHAR(24), nullable=False, unique=True)


class Language(Base):
    __tablename__: str = "languages"

    id = Column(SmallInteger, primary_key=True)
    language_code = Column(CHAR(2), nullable=False, unique=True)


class BotUser(Base):
    __tablename__: str = "bot_users"

    id = Column(SmallInteger, primary_key=True)
    is_blocked = Column(Boolean, default=False)
    balance = Column(DECIMAL(7, 2), default=0.00)
    language_id = Column(SmallInteger, ForeignKey("languages.id", ondelete="SET NULL"))


class Status(Base):
    __tablename__: str = "statuses"

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)


class Invoice(Base):
    __tablename__: str = "invoices"

    id = Column(SmallInteger, primary_key=True)
    bot_user_id = Column(SmallInteger, ForeignKey("bot_users.id", ondelete="NO ACTION"))
    date_create = Column(TIMESTAMP, default=datetime.now())
    status_id = Column(SmallInteger, ForeignKey("statuses.id", ondelete="NO ACTION"))


class Order(Base):
    __tablename__: str = "orders"

    id = Column(SmallInteger, primary_key=True)
    bot_user_id = Column(SmallInteger, ForeignKey("bot_users.id", ondelete="NO ACTION"))
    date_create = Column(TIMESTAMP, default=datetime.now())
    status_id = Column(SmallInteger, ForeignKey("statuses.id", ondelete="NO ACTION"))
    invoice_id = Column(SmallInteger, ForeignKey("invoices.id", ondelete="NO ACTION"))


class OrderItem(Base):
    __tablename__: str = "order_items"

    id = Column(SmallInteger, primary_key=True)
    order_id = Column(SmallInteger, ForeignKey("orders.id", ondelete="NO ACTION"))
    product_id = Column(SmallInteger, ForeignKey("products.id", ondelete="NO ACTION"))
    total = Column(DECIMAL(7, 2))


class User(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(24), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)

