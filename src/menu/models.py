from typing import List, Optional
import enum
from sqlalchemy import Table, Enum, Column, ForeignKey, String, Integer
from sqlalchemy.orm import mapped_column, relationship, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class CategoryEnum(Enum):
    BAR = "Bar"
    KITCHEN = "Kitchen"


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    restaurants: Mapped[List["Restaurant"]] = relationship(back_populates="user")


class RestaurantMenuAssociation(Base):
    __tablename__ = "restaurant_menu_association"

    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurant_table.id"), primary_key=True)
    menu_id: Mapped[int] = mapped_column(ForeignKey("menu_table.id"), primary_key=True)
    restaurant: Mapped["Restaurant"] = relationship(back_populates="menu_associations")
    menu: Mapped["Menu"] = relationship(back_populates="restaurant_associations")


class Restaurant(Base):
    """class для ресторана"""
    __tablename__ = 'restaurant_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    user_id: [Mapped[User]] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="restaurants")
    menus: Mapped[List["Menu"]] = relationship(
        secondary="restaurant_menu_association", back_populates='restaurants'
    )
    menu_associations: Mapped[List["RestaurantMenuAssociation"]] = relationship(back_populates="restaurant")
# todo Изменить схему на M2M
# todo Добавить поле bool поле is_active
# todo Подумать, нужно ли добавить адрес ресторана
# todo добавить __repr__ методы для классов


class Menu(Base):
    """Класс меню(может быть сезонное меню, банкетное и т.д.)"""
    __tablename__ = "menu_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    categories: Mapped[List["Category"]] = relationship(back_populates="menu")
    restaurants: Mapped[List["Restaurant"]] = relationship(
        secondary="restaurant_menu_association", back_populates='menus'
    )
    restaurant_associations: Mapped[List["RestaurantMenuAssociation"]] = relationship(back_populates="menu")


class Category(Base):
    """Категории меню(Основные блюда, горячие закуски, первые блюда и т.д.)"""
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    section = mapped_column(Enum(CategoryEnum))
    menu_id: Mapped[int] = ForeignKey("menu.id")
# todo продумать связь для блюда и категории чтобы одно блюда можно было использовать в другом меню


class ItemCompoundAssociations(Base):
    __tablename__ = "item_compound_associations"

    item_id: Mapped[int] = mapped_column(ForeignKey("item_table.id"), primary_key=True)
    compound_id: Mapped[int] = mapped_column(ForeignKey("compound_table.id"), primary_key=True)
    item: Mapped["Item"] = relationship(back_populates="compound_associations")
    compound: Mapped["Compound"] = relationship(back_populates="item_associations")


class Item(Base):
    """Позиция в меню(Бифштекс, Мохито, Паста и т.д.)"""
    __tablename__ = "item_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    weight: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    compounds: Mapped[List["Compound"]] = relationship(
        secondary="item_compound_associations",
        back_populates="item"
    )
    compound_associations: Mapped[List["ItemCompoundAssociations"]] = relationship(back_populates="item")


class Compound(Base):
    """Класс для ингредиентов блюда(Лук, картофель, сметана, перец и т.д.)"""
    __tablename__ = "compound_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    items = relationship(
        secondary="item_compound_associations",
        back_populates="compound"
    )
    item_associations: Mapped[List["ItemCompoundAssociations"]] = relationship(back_populates="compound")
    # todo узнать почему на схеме в связующей таблице указан column amount
