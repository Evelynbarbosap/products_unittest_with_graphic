from fastapi import HTTPException
from domain.models.product import db_products


class ValidatorProduct:
    def validate_product_not_exists(product_id):
        if product_id not in db_products:
            raise HTTPException(status_code=404, detail="Product not found.")

    def validate_name_is_required(name):
        if name is None:
            raise HTTPException(status_code=422,
                                detail="The name field name is required.")

    def validate_name_maximum_character(name):
        if len(name) > 30:
            raise HTTPException(status_code=422,
                                detail="The name field needs a maximum of 20 characters.")

    def validate_description_maximum_character(description):
        if len(description) >= 500:
            raise HTTPException(status_code=422,
                                detail="The descrition field needs a maximum of 500 characters.")

    def validate_minimum_price(price):
        if price <= 0.00 or price is None:
            raise HTTPException(status_code=422,
                                detail="the price field needs a value above 0.00")
