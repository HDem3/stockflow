from sqlalchemy.orm import Session

from app import models, schemas

# funzione di servizio per la creazione di un nuovo prodotto
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

# funzione di servizio per il recupero di tutti i prodotti
def get_products(db: Session):

    return db.query(models.Product).all()

# funzione di servizio per il recupero di un prodotto specifico per ID
def get_product_by_id(db: Session, product_id: int):

    return db.query(models.Product).filter(
        models.Product.id == product_id).first()

def update_product(db: Session, product: models.Product, 
                   updated_product: schemas.ProductCreate):

    product.name = updated_product.name
    product.sku = updated_product.sku
    product.description = updated_product.description
    product.price = updated_product.price
    product.quantity = updated_product.quantity

    db.commit()
    db.refresh(product)

    return product

# funzione di servizio per la cancellazione di un prodotto specifico per ID
def delete_product(db: Session, product: models.Product):
    db.delete(product)
    db.commit()

# funzione di servizio per il recupero dei prodotti con quantità inferiore o uguale a una soglia specificata
def get_low_stock_products(db: Session, threshold: int):

    return db.query(models.Product).filter(models.Product.quantity <= threshold).all()


    

