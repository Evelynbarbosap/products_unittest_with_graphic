import unittest
from fastapi.testclient import TestClient
from main import products_router
from fastapi import HTTPException

client = TestClient(products_router)


class TestProductAPI(unittest.TestCase):
    def test_get_products(self):
        response = client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_product(self):
        response = client.get("/products/1")
        self.assertEqual(response.status_code, 200)
        expected_product = {
            "name": "Smartphone",
            "description": "Um celular bacana",
            "price": 1999.99,
            "available": True
        }
        product_data = response.json()
        self.assertEqual(product_data, expected_product)

        self.assertIsInstance(product_data["name"], str)
        self.assertIsInstance(product_data["description"], str)
        self.assertIsInstance(product_data["price"], float)
        self.assertIsInstance(product_data["available"], bool)

    def test_get_nonexistent_product(self):
        try:
            response = client.get("/products/999")
            self.assertEqual(response.status_code, 404)

        except HTTPException as e:
            self.assertEqual(e.status_code, 404)
            pass

    def test_create_product(self):
        new_product_data = {
            "name": "New Product",
            "description": "Description of New Product",
            "price": 29.99,
            "available": True
        }
        response = client.post("/products/", json=new_product_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), new_product_data)

    def test_update_product(self):
        updated_product_data = {
            "name": "Updated Product",
            "description": "Updated Description",
            "price": 19.99,
            "available": False
        }
        response = client.put("/products/1", json=updated_product_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), updated_product_data)

    def test_update_nonexistent_product(self):
        updated_product_data = {
            "name": "Updated Product",
            "description": "Updated Description",
            "price": 19.99,
            "available": False
        }

        try:
            response = client.put("/products/999", json=updated_product_data)
            self.assertEqual(response.status_code, 404)

        except HTTPException as e:
            self.assertEqual(e.status_code, 404)
            pass

    def test_delete_product(self):
        response = client.delete("/products/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Product deleted successfully.")

    def test_delete_nonexistent_product(self):
        try:
            response = client.delete("/products/999")
            self.assertEqual(response.status_code, 404)

        except HTTPException as e:
            self.assertEqual(e.status_code, 404)
            pass


if __name__ == '__main__':
    unittest.main()
