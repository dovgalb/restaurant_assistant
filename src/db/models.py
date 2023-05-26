from typing import List, Optional
from sqlalchemy import Table, Enum, Column, ForeignKey, String, Integer
from sqlalchemy.orm import mapped_column, relationship, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


# class CategoryEnum(Enum):
#     BAR = "Bar"
#     KITCHEN = "Kitchen"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    restaurants: Mapped[List["Restaurant"]] = relationship(back_populates="user")


class RestaurantMenuAssociations(Base):
    __tablename__ = "restaurant_menu_associations"

    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"), primary_key=True)
    menu_id: Mapped[int] = mapped_column(ForeignKey("menus.id"), primary_key=True)
    restaurant: Mapped["Restaurant"] = relationship(back_populates="menu_associations")
    menu: Mapped["Menu"] = relationship(back_populates="restaurant_associations")


class Restaurants(Base):
    """class для ресторана"""
    __tablename__ = 'restaurants'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    user_id: Mapped[Users] = mapped_column(ForeignKey("users.id"))

    user: Mapped["Users"] = relationship(back_populates="restaurants")
    menus: Mapped[List["Menus"]] = relationship(
        secondary="restaurant_menu_association", back_populates='restaurants'
    )
    menu_associations: Mapped[List["RestaurantMenuAssociations"]] = relationship(back_populates="restaurant")
# todo Изменить схему на M2M
# todo Добавить поле bool поле is_active
# todo Подумать, нужно ли добавить адрес ресторана
# todo добавить __repr__ методы для классов


class Menus(Base):
    """Класс меню(может быть сезонное меню, банкетное и т.д.)"""
    __tablename__ = "menus"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    categories: Mapped[List["Categories"]] = relationship(back_populates="db")
    restaurants: Mapped[List["Restaurants"]] = relationship(
        secondary="restaurant_menu_association", back_populates='menus'
    )
    restaurant_associations: Mapped[List["RestaurantMenuAssociations"]] = relationship(back_populates="db")


class Categories(Base):
    """Категории меню(Основные блюда, горячие закуски, первые блюда и т.д.)"""
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    section = mapped_column(Enum("Bar", "Kitchen"), nullable=False)
    menu_id: Mapped[int] = ForeignKey("db.id")
# todo продумать связь для блюда и категории чтобы одно блюда можно было использовать в другом меню


class ItemCompoundAssociations(Base):
    """Ассоциативный класс для связи таблиц item_table и compound_table"""
    __tablename__ = "item_compound_associations"

    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), primary_key=True)
    compound_id: Mapped[int] = mapped_column(ForeignKey("compounds.id"), primary_key=True)
    item: Mapped["Items"] = relationship(back_populates="compound_associations")
    compound: Mapped["Compounds"] = relationship(back_populates="item_associations")


class Items(Base):
    """Позиция в меню(Бифштекс, Мохито, Паста и т.д.)"""
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    weight: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    compounds: Mapped[List["Compounds"]] = relationship(
        secondary="item_compound_associations",
        back_populates="item"
    )
    compound_associations: Mapped[List["ItemCompoundAssociations"]] = relationship(back_populates="item")


class Compounds(Base):
    """Класс для ингредиентов блюда(Лук, картофель, сметана, перец и т.д.)"""
    __tablename__ = "compounds"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    items: Mapped[List["Items"]] = relationship(
        secondary="item_compound_associations",
        back_populates="compound"
    )
    item_associations: Mapped[List["ItemCompoundAssociations"]] = relationship(back_populates="compound")
    # todo узнать почему на схеме в связующей таблице указан column amount
