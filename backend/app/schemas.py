from pydantic import BaseModel
from typing import List

class ItemBase(BaseModel):
    """Базовая схема для Item"""
    caption: str

class ItemCreate(ItemBase):
    """Схема для создания Item"""
    pass

class Item(ItemBase):
    """Схема для отображения Item"""
    id: int

    class Config:
        from_attributes = True

class ItemsResponse(BaseModel):
    """Схема для ответа со списком items"""
    items: List[Item]
    total: int
