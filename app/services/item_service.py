# app/services/item_service.py
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

class ItemService:
    @staticmethod
    def get(db: Session, item_id: int) -> Optional[Item]:
        return db.query(Item).filter(Item.id == item_id).first()

    @staticmethod
    def get_multi(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
        return db.query(Item).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, item_in: ItemCreate) -> Item:
        db_item = Item(**item_in.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def update(db: Session, item: Item, item_in: ItemUpdate) -> Item:
        for field, value in item_in.dict(exclude_unset=True).items():
            setattr(item, field, value)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def delete(db: Session, item_id: int) -> Item:
        item = db.query(Item).filter(Item.id == item_id).first()
        if item:
            db.delete(item)
            db.commit()
        return item