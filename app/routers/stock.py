from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db


router= APIRouter(
    prefix="/stock", 
    tags=["Stock"]
)

@router.post("/in", response_model=schemas.ProductResponse)
def stock_in(movement: schemas.StockMovement, 
             db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == movement.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.quantity += movement.quantity

    db.commit()
    db.refresh(product)

    return product

@router.post("/out", response_model=schemas.ProductResponse)
def stock_out(movement: schemas.StockMovement, 
             db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == movement.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.quantity < movement.quantity:
        raise HTTPException(
            status_code=400,
            detail="Stock insufficiente"
        )

    product.quantity -= movement.quantity

    db.commit()
    db.refresh(product)

    return product

