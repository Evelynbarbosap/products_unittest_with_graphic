from pydantic import BaseModel
from typing import Dict


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    available: bool


db_products: Dict[int, Product] = {
    1: Product(id=1, name="Smartphone", description="A cool cell phone",
               price=1999.99, available=True),
    2: Product(id=2, name="Notebook", description="A laptop computer",
               price=3999.99, available=False),
    3: Product(id=3, name="Refrigerator", description="Brastemp", price=3999.99,
               available=False),
}
