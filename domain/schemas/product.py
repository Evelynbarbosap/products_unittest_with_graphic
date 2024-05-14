from pydantic import BaseModel, Field, validator
from typing import Optional
from domain.validators.product import ValidatorProduct


class ProductListOutPut(BaseModel):
    id: int = Field(title="Product ID")
    name: str = Field(title="Product name")
    price: float = Field(title="Product price")
    available: bool = Field(title="Product available")


class ProductOutPut(BaseModel):
    name: str = Field(title="Product name")
    description: str = Field(title="Product description")
    price: float = Field(title="Product price")
    available: bool = Field(title="Product available")


class ProductCreate(BaseModel):
    name: str = Field(title="Product name")
    description: Optional[str] = Field(title="Product description")
    price: float = Field(title="Product price")
    available: bool = Field(title="Product available")

    @validator('name')
    def validator_name(cls, v):
        ValidatorProduct.validate_name_is_required(name=v)
        ValidatorProduct.validate_name_maximum_character(name=v)

        return v

    @validator('description')
    def validator_description(cls, v):
        ValidatorProduct.validate_description_maximum_character(description=v)

        return v

    @validator('price')
    def validator_price(cls, v):
        ValidatorProduct.validate_minimum_price(price=v)

        return v


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(title="Product name")
    description: Optional[str] = Field(title="Product")
    price: Optional[float] = Field(title="Product price")
    available: Optional[bool] = Field(title="Product available")

    @validator('name')
    def validator_name(cls, v):
        ValidatorProduct.validate_name_maximum_character(name=v)

        return v

    @validator('description')
    def validator_description(cls, v):
        ValidatorProduct.validate_description_maximum_character(description=v)

        return v

    @validator('price')
    def validator_price(cls, v):
        ValidatorProduct.validate_minimum_price(price=v)

        return v
