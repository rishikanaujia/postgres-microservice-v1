# app/api/v1/endpoints/items.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.services.item_service import ItemService

router = APIRouter()

@router.get("/", response_model=List[Item])
def read_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> List[Item]:
    return ItemService.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: ItemCreate,
) -> Item:
    return ItemService.create(db, item_in=item_in)

@router.get("/{item_id}", response_model=Item)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
) -> Item:
    item = ItemService.get(db, item_id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return item

@router.put("/{item_id}", response_model=Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
    item_in: ItemUpdate,
) -> Item:
    item = ItemService.get(db, item_id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return ItemService.update(db, item=item, item_in=item_in)

@router.delete("/{item_id}", response_model=Item)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
) -> Item:
    item = ItemService.get(db, item_id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return ItemService.delete(db, item_id=item_id)