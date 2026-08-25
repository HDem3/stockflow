from sqlalchemy.orm import Session

from app import models, schemas


def create_product(db: Session, product: schemas.ProductCreate):
    new_product = models.Product(
            name= product.name,
            sku= product.sku,
            description= product.description,
            price= product.price,
            quantity= product.quantity
        )
    
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
    return new_product

def get_products(db: Session):

    return db.query(models.Product).all()