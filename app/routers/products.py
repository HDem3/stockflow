from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.services import product_service

#prefissi e tag
router= APIRouter(
    prefix="/products", 
    tags=["Products"]
)

# creazione di un nuovo prodotto
@router.post("", response_model=schemas.ProductResponse)
async def create_product(product: schemas.ProductCreate, 
                         db: Session = Depends(get_db)):

    return product_service.create_product(db, product)

# recupero di tutti i prodotti
@router.get("", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    
    return product_service.get_products(db)

# recupero di un prodotto specifico per ID
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):

    product = product_service.get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

# aggiornamento di un prodotto specifico per ID
@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, updated_product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = product_service.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product = product_service.update_product(db, product, updated_product)

    return product

# eliminazione di un prodotto specifico per ID
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):

    product = product_service.get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product_service.delete_product(db, product)
    
    return {"message": "Product deleted successfully"}

@router.get("/low-stock/{threshold}", response_model=list[schemas.ProductResponse])
def get_low_stock_products(threshold: int, db: Session = Depends(get_db)):
    
    return product_service.get_low_stock_products(db, threshold)
