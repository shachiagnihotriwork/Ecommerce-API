from fastapi import Depends, FastAPI
from models import Product
from database import session, engine, Base
import dbmodels
from sqlalchemy.orm import Session
app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get('/')
def greet():
    return 'Welcome to home page'



def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(dbmodels.Product).count()
    if count == 0:

        for product in products:
            db.add(dbmodels.Product(**product.model_dump()))
        db.commit()
init_db()


@app.get('/allproducts')
def get_all_products(db : Session = Depends(get_db)):
    db_products = db.query(dbmodels.Product).all()
    return db_products

@app.get('/product/{id}')
def get_product_id(id:int,db : Session = Depends(get_db)):
    db_products = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if db_products:
        return db_products
        
    return "No product is registered from this id"

@app.post('/product')
def add_product(product: Product,db:Session = Depends(get_db)):
    db_products = db.add(dbmodels.Product(**product.model_dump()))
    db.commit()
    return db_products

@app.put('/product')
def update_product(id : int , product : Product, db:Session = Depends(get_db)):
    db_products = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if db_products:
        db_products.name = product.name 
        db_products.description = product.description
        db_products.price = product.price
        db_products.qty = product.qty
        db.commit()        
        return "Product added successfully"
    return "Product not found"

@app.delete('/product')
def del_product(id : int, db:Session = Depends(get_db)):
    db_products = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if db_products:
        db.delete(db_products)
        db.commit()
        return "Product deleted successfully"
    return "Product not found"