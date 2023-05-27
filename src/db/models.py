from datetime import datetime
from typing import List, Optional
from sqlalchemy import Enum, ForeignKey, String, Integer, Boolean, TIMESTAMP
from sqlalchemy.orm import mapped_column, relationship, Mapped

from src.db.base import Base


# class CategoryEnum(Enum):
#     BAR = "Bar"
#     KITCHEN = "Kitchen"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    restaurants: Mapped[List["Restaurants"]] = relationship(back_populates="user")


class RestaurantMenuAssociations(Base):
    __tablename__ = "restaurant_menu_associations"

    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"), primary_key=True)
    menu_id: Mapped[int] = mapped_column(ForeignKey("menus.id"), primary_key=True)
    restaurant: Mapped["Restaurants"] = relationship(back_populates="menu_associations")
    menu: Mapped["Menus"] = relationship(back_populates="restaurant_associations")


class Restaurants(Base):
    """class для ресторана"""
    __tablename__ = 'restaurants'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(350), nullable=True)
    created_at = mapped_column(TIMESTAMP, default=datetime.utcnow)
    updated_at = mapped_column(TIMESTAMP, onupdate=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    user_id: Mapped[Users] = mapped_column(ForeignKey("users.id"))

    user: Mapped["Users"] = relationship(back_populates="restaurants")
    menus: Mapped[List["Menus"]] = relationship(
        secondary="restaurant_menu_associations", back_populates='restaurants'
    )
    menu_associations: Mapped[List["RestaurantMenuAssociations"]] = relationship(back_populates="restaurant",
                                                                                 viewonly=True)


# todo добавить __repr__ методы для классов


class Menus(Base):
    """Класс меню(может быть сезонное меню, банкетное и т.д.)"""
    __tablename__ = "menus"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(350))
    created_at = mapped_column(TIMESTAMP, default=datetime.utcnow)
    updated_at = mapped_column(TIMESTAMP, onupdate=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    categories: Mapped[List["Categories"]] = relationship(back_populates="menu")
    restaurants: Mapped[List["Restaurants"]] = relationship(
        secondary="restaurant_menu_associations", back_populates='menus'
    )
    restaurant_associations: Mapped[List["RestaurantMenuAssociations"]] = relationship(back_populates="menu",
                                                                                       viewonly=True)


class Categories(Base):
    """Категории меню(Основные блюда, горячие закуски, первые блюда и т.д.)"""
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    section = mapped_column(Enum("Bar", "Kitchen", name="section_enum"), nullable=False)
    menu_id: Mapped[int] = mapped_column(ForeignKey("menus.id"))
    menu: Mapped["Menus"] = relationship(back_populates="categories")
    category_associations: Mapped[List["ItemCategoryAssociations"]] = relationship(back_populates="category")


# todo продумать связь для блюда и категории чтобы одно блюда можно было использовать в другом меню


class ItemCompoundAssociations(Base):
    """Ассоциативный класс для связи таблиц item_table и compound_table"""
    __tablename__ = "item_compound_associations"

    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), primary_key=True)
    compound_id: Mapped[int] = mapped_column(ForeignKey("compounds.id"), primary_key=True)
    amount: Mapped[int] = mapped_column(Integer, comment="Кол-во грамм продукта")
    item: Mapped["Items"] = relationship(back_populates="compound_associations")
    compound: Mapped["Compounds"] = relationship(back_populates="item_associations")


class ItemCategoryAssociations(Base):
    """Ассоциативный класс для связи таблиц item_table и category_table"""
    __tablename__ = "item_category_associations"

    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)
    item: Mapped["Items"] = relationship(back_populates="category_associations")
    category: Mapped["Categories"] = relationship(back_populates="category_associations")


class Items(Base):
    """Позиция в меню(Бифштекс, Мохито, Паста и т.д.)"""
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    weight: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    compounds: Mapped[List["Compounds"]] = relationship(
        secondary="item_compound_associations",
        back_populates="items"
    )
    compound_associations: Mapped[List["ItemCompoundAssociations"]] = relationship(back_populates="item")
    category_associations: Mapped[List["ItemCategoryAssociations"]] = relationship(back_populates="item")


class Compounds(Base):
    """Класс для ингредиентов блюда(Лук, картофель, сметана, перец и т.д.)"""
    __tablename__ = "compounds"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    items: Mapped[List["Items"]] = relationship(
        secondary="item_compound_associations",
        back_populates="compounds"
    )
    item_associations: Mapped[List["ItemCompoundAssociations"]] = relationship(back_populates="compound")
