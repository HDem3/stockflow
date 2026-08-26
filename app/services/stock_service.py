
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db


def create_stockMovement(db: Session,product_id: int, movement: schemas.StockMovementCreate):

    product= db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    new_quantity= product.quantity + movement.quantity_change

    if new_quantity < 0:
        raise HTTPException(status_code=400, detail="Insufficient stock for this operation")

    stock_movement = models.StockMovement(
        product_id= product_id,
        quantity_change= movement.quantity_change,
        reason= movement.reason
    )

    product.quantity = new_quantity

    db.add(stock_movement)
    db.commit()
    db.refresh(stock_movement)

    return stock_movement