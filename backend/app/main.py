from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import logging

from . import models, schemas
from .database import engine, get_db

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание таблиц
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple App API", version="1.0.0")

# Настройка CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://frontend:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Инициализация при запуске"""
    logger.info("🚀 Starting Simple App API")
    
    # Создаем тестовые данные
    db = next(get_db())
    
    # Проверяем, есть ли уже данные
    existing_count = db.query(models.Item).count()
    
    if existing_count == 0:
        logger.info("📝 Creating initial test data")
        test_items = [
            models.Item(caption="Первая запись"),
            models.Item(caption="Вторая запись"),
            models.Item(caption="Третья запись"),
            models.Item(caption="Четвертая запись"),
            models.Item(caption="Пятая запись"),
        ]
        
        for item in test_items:
            db.add(item)
        
        db.commit()
        logger.info(f"✅ Created {len(test_items)} test items")
    else:
        logger.info(f"📊 Found {existing_count} existing items")

@app.get("/")
async def root():
    """Корневой маршрут"""
    return {
        "message": "Simple App API", 
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Проверка здоровья API"""
    return {"status": "healthy", "service": "simple-app-api"}

@app.get("/api/items", response_model=schemas.ItemsResponse)
async def get_items(db: Session = Depends(get_db)):
    """Получение всех записей из таблицы items"""
    try:
        items = db.query(models.Item).all()
        logger.info(f"📊 Retrieved {len(items)} items from database")
        
        return schemas.ItemsResponse(
            items=items,
            total=len(items)
        )
    except Exception as e:
        logger.error(f"❌ Error retrieving items: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/api/items", response_model=schemas.Item)
async def create_item(
    item: schemas.ItemCreate, 
    db: Session = Depends(get_db)
):
    """Создание новой записи"""
    try:
        db_item = models.Item(caption=item.caption)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        logger.info(f"✅ Created new item: {db_item.caption}")
        return db_item
    except Exception as e:
        logger.error(f"❌ Error creating item: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.delete("/api/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Удаление записи по ID"""
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
        
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        db.delete(item)
        db.commit()
        
        logger.info(f"🗑️ Deleted item with ID: {item_id}")
        return {"message": "Item deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error deleting item: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/api/items/{item_id}", response_model=schemas.Item)
async def get_item(item_id: int, db: Session = Depends(get_db)):
    """Получение записи по ID"""
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
        
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        return item
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error retrieving item: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
