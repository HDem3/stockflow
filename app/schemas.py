from pydantic import BaseModel, ConfigDict, Field #stile json


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

class StockMovementCreate(BaseModel):
    quantity_change: int = Field(gt=0)
    reason: str

class StockMovementResponse(BaseModel):
    id: int
    product_id: int
    quantity_change: int
    reason: str
    created_at: str

    model_config = ConfigDict(from_attributes= True) #uguale a quello sopra questo piu adatto per pydantic
    
