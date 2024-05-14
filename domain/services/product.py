from domain.validators.product import ValidatorProduct
from domain.models.product import db_products, Product


class ProductService:
    def get_all_product():
        return list(db_products.values())

    def get_product_by_id(product_id):
        ValidatorProduct.validate_product_not_exists(product_id=product_id)

        return db_products[product_id]

    def create_product(product):
        index = len(db_products) + 1

        db_products[index] = Product(
            id=index,
            name=product.name,
            description=product.description,
            price=product.price,
            available=product.available
        )

        return product

    def update_product(product_id, product):
        ValidatorProduct.validate_product_not_exists(product_id=product_id)

        db_products[product_id] = product

        return product

    def delete_product(product_id: int):
        ValidatorProduct.validate_product_not_exists(product_id=product_id)

        del db_products[product_id]

        return {"message": "Product deleted successfully."}
