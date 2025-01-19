# app/schemas/item.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class ItemInDBBase(ItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class Item(ItemInDBBase):
    pass