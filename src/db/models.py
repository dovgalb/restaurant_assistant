from sqlalchemy import ForeignKey, String, Integer, Boolean, TIMESTAMP, DateTime, Column, LargeBinary, UniqueConstraint
from sqlalchemy.orm import mapped_column, relationship, Mapped, backref
from sqlalchemy.sql import func

from src.db.base import Base


class User(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True)

    restaurants = relationship("Restaurant", back_populates="user")


class RestaurantMenu(Base):
    __tablename__ = "restaurant_menu"
    # id = mapped_column(Integer, primary_key=True)

    restaurant_id = mapped_column(Integer, ForeignKey("restaurants.id"), primary_key=True)
    menu_id = mapped_column(Integer, ForeignKey("menus.id"), primary_key=True)


class Restaurant(Base):
    __tablename__ = "restaurants"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), unique=True, index=True)
    description = mapped_column(String, nullable=True)
    address = mapped_column(String, unique=True, nullable=True)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=func.now())
    is_active = mapped_column(Boolean, default=True)

    user_id = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="restaurants")
    menus = relationship("Menu", secondary=RestaurantMenu.__table__, back_populates="restaurants")


class Menu(Base):
    __tablename__ = "menus"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), unique=True, index=True)
    description = mapped_column(String, nullable=True)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=func.now())
    is_active = mapped_column(Boolean, default=True)

    restaurants = relationship("Restaurant", secondary=RestaurantMenu.__table__, back_populates="menus")
    categories = relationship("Category", back_populates="menu")


class Category(Base):
    __tablename__ = 'categories'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, unique=True)
    is_active = mapped_column(Boolean, default=True)

    menu_id = mapped_column(Integer, ForeignKey("menus.id"))
    menu = relationship("Menu", back_populates="categories")
    subcategories = relationship("Subcategory", back_populates="category")


class Subcategory(Base):
    __tablename__ = "subcategories"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, unique=True, index=True)

    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="subcategories")
    dishes = relationship("Dish", back_populates="subcategory")


class DishIngredient(Base):
    __tablename__ = "dish_ingredient"
    id = mapped_column(Integer, primary_key=True)

    amount = mapped_column(Integer, nullable=False)

    dish_id = mapped_column(Integer, ForeignKey("dishes.id"), primary_key=True)
    ingredient_id = mapped_column(Integer, ForeignKey("ingredients.id"), primary_key=True)

    # ingredient = relationship("Ingredient")
    # dish = relationship("Dish")


class Dish(Base):
    __tablename__ = "dishes"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, unique=True, index=True)
    description = mapped_column(String, nullable=True)
    weight = mapped_column(Integer, nullable=True)
    price = mapped_column(Integer)
    photo = mapped_column(LargeBinary, nullable=False)
    is_active = mapped_column(Boolean, default=True)

    subcategory_id = mapped_column(Integer, ForeignKey('subcategories.id'))
    subcategory = relationship("Subcategory", back_populates='dishes')
    ingredients = relationship("Ingredient", secondary=DishIngredient.__table__, back_populates='dishes')


class Ingredient(Base):
    __tablename__ = "ingredients"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, unique=True, index=True)
    unit = mapped_column(String(3), nullable=True)

    parent_id = mapped_column(Integer, ForeignKey("ingredients.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    sub_ingredients = relationship("Ingredient", cascade="all, delete-orphan", backref=backref("sub_ingredients_ingredients", remote_side=[id]))
    dishes = relationship("Dish", secondary=DishIngredient.__table__, back_populates='ingredients')




