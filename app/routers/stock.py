from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_db
from app.services import stock_service

router= APIRouter(
    tags=["Stock"]
)



@router.post("/products/{product_id}/stock", response_model=schemas.StockMovementResponse)
def create_stock_movement(product_id: int, 
                          movement: schemas.StockMovementCreate, 
                          db: Session = Depends(get_db)):

    return stock_service.create_stockMovement(db, product_id, movement)

@router.get("/stock/movements", response_model=list[schemas.StockMovementResponse])
def get_stock_movements(db: Session = Depends(get_db)):

    return stock_service.get_stockMovements(db)