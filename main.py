from fastapi import FastAPI
from models import Product
from database import session, engine, Base
import dbmodels
app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get('/')
def greet():
    return 'Welcome to home page'

products = [
    Product(id = 1 , name = 'iPhone12', description = 'budget phone', price = 999, qty = 36),
    Product(id = 2 , name = 'hp laptop', description = 'budget laptop', price = 1999, qty = 11),
    Product(id = 3 , name = 'iPad', description = 'tablet', price = 4999, qty = 15),
    Product(id = 4 , name = 'samsung', description = 'latest phone', price = 1299, qty = 34)
]

@app.get('/allproducts')
def get_all_products():
    return products

@app.get('/product/{id}')
def get_product_id(id:int):
    for product in products:
        if product.id == id:
            return product
        
    return "No product is registered from this id"

@app.post('/product')
def add_product(product: Product):
    products.append(product)
    return product

@app.put('/product')
def update_product(id : int , product : Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added successfully"
    return "Product not found"

@app.delete('/product')
def del_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully"
    return "Product not found"