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


restaurant_menu_association_table = Table(
    'restaurant_menu_association_table',
    Base.metadata,
    Column("restaurant_id", ForeignKey("restaurant.id"), primary_key=True),
    Column("menu_id", ForeignKey("menu.id"), primary_key=True)
)


item_compound_association_table = Table(
    "item_compound_association_table",
    Base.metadata,
    Column("item_id", ForeignKey("item.id"), primary_key=True),
    Column("compound_id", ForeignKey("compound.id"), primary_key=True)
)
# todo узнать почему на схеме в связующей таблице указан column amount


class Restaurant(Base):
    """class для ресторана"""
    __tablename__ = 'restaurant'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    user_id: [Mapped[User]] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="restaurants")
    menus: Mapped[List["Menu"]] = relationship(
        secondary=restaurant_menu_association_table, back_populates='restaurants'
    )
# todo Изменить схему на M2M
# todo Добавить поле bool поле is_active
# todo Подумать, нужно ли добавить адрес ресторана
# todo добавить __repr__ методы для классов


class Menu(Base):
    """Класс меню(может быть сезонное меню, банкетное и т.д.)"""
    __tablename__ = "menu"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    categories: Mapped[List["Category"]] = relationship(back_populates="menu")
    restaurants: Mapped[List[Restaurant]] = relationship(
        secondary=restaurant_menu_association_table, back_populates='menus'
    )


class Category(Base):
    """Категории меню(Основные блюда, горячие закуски, первые блюда и т.д.)"""
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    section = mapped_column(Enum(CategoryEnum))
    menu_id: Mapped[int] = ForeignKey("menu.id")
# todo продумать связь для блюда и категории чтобы одно блюда можно было использовать в другом меню


class Item(Base):
    """Позиция в меню(Бифштекс, Мохито, Паста и т.д.)"""
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    weight: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    compounds = relationship(
        "Compound",
        secondary="item_compound_association_table",
        back_populates="items"
    )


class Compound(Base):
    """Класс для ингредиентов блюда(Лук, картофель, сметана, перец и т.д.)"""
    __tablename__ = "compound"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    items = relationship(
        "Item",
        secondary="item_compound_association_table",
        back_populates="compounds"
    )