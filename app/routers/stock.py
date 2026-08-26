from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_db
from app.services import stock_service

router= APIRouter(
    prefix="/products/{product_id}", 
    tags=["Stock"]
)

@router.post("/stock", response_model=schemas.StockMovementResponse)
def create_stock_movement(product_id: int, 
                          movement: schemas.StockMovementCreate, 
                          db: Session = Depends(get_db)):

    return stock_service.create_stockMovement(db, product_id, movement)