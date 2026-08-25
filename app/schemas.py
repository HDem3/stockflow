from pydantic import BaseModel #stile json


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