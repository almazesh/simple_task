from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Simple App API", version="1.0.0")

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Простые модели без SQLAlchemy
class ItemCreate(BaseModel):
    caption: str

class Item(BaseModel):
    id: int
    caption: str

class ItemsResponse(BaseModel):
    items: List[Item]
    total: int

# Временное хранилище в памяти
items_storage = [
    {"id": 1, "caption": "Первая запись"},
    {"id": 2, "caption": "Вторая запись"},
    {"id": 3, "caption": "Третья запись"},
]

@app.get("/")
async def root():
    return {"message": "Simple App API", "version": "1.0.0", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "simple-app-api"}

@app.get("/api/items", response_model=ItemsResponse)
async def get_items():
    """Получение всех записей"""
    logger.info(f"📊 Retrieved {len(items_storage)} items")
    return ItemsResponse(items=items_storage, total=len(items_storage))

@app.post("/api/items", response_model=Item)
async def create_item(item: ItemCreate):
    """Создание новой записи"""
    new_id = max([i["id"] for i in items_storage], default=0) + 1
    new_item = {"id": new_id, "caption": item.caption}
    items_storage.append(new_item)
    
    logger.info(f"✅ Created new item: {item.caption}")
    return new_item

@app.delete("/api/items/{item_id}")
async def delete_item(item_id: int):
    """Удаление записи по ID"""
    global items_storage
    items_storage = [item for item in items_storage if item["id"] != item_id]
    
    logger.info(f"🗑️ Deleted item with ID: {item_id}")
    return {"message": "Item deleted successfully"}

@app.get("/api/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Получение записи по ID"""
    item = next((item for item in items_storage if item["id"] == item_id), None)
    if not item:
        return {"error": "Item not found"}
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)