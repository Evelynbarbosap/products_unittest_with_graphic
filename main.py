from fastapi import FastAPI
from domain.routers import products

app = FastAPI()

products_router = products.router
app.include_router(products_router)
