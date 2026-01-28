from fastapi import FastAPI
from models import Product
app = FastAPI()

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