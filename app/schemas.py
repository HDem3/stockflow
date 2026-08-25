from pydantic import BaseModel, Field #stile json


class ProductCreate(BaseModel):
    name: str
    sku: str
    description: str | None = None
    price: float
    quantity: int

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    description: str | None = None
    price: float
    quantity: int

    model_config = {
        "from_attributes": True
    }

class StockMovement(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    
