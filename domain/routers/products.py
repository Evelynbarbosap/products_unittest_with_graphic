from domain.schemas.product import ProductListOutPut, ProductOutPut, \
    ProductCreate, ProductUpdate
from typing import List
from domain.services.product import ProductService
from fastapi import APIRouter

router = APIRouter(tags=["Products"])


@router.get("/products/", response_model=List[ProductListOutPut])
def get_products():
    """Get all products"""
    products = ProductService.get_all_product()

    return products


@router.get("/products/{product_id}", response_model=ProductOutPut)
def get_product(product_id: int):
    """Get product by ID"""
    product = ProductService.get_product_by_id(product_id=product_id)

    return product


@router.post("/products/", response_model=ProductOutPut)
def create_product(product: ProductCreate):
    """Create product"""
    created = ProductService.create_product(product=product)

    return created


@router.put("/products/{product_id}", response_model=ProductOutPut)
def update_product(product_id: int, product: ProductUpdate):
    """Update product"""
    updated = ProductService.update_product(product_id=product_id,
                                            product=product)

    return updated


@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Delete product"""
    deleted = ProductService.delete_product(product_id=product_id)

    return deleted["message"]
