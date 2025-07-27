from sqlalchemy import Column, Integer, String
from .database import Base

class Item(Base):
    """Модель таблицы items с полями id и caption"""
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    caption = Column(String(255), nullable=False, index=True)

    def __repr__(self):
        return f"<Item(id={self.id}, caption='{self.caption}')>"
