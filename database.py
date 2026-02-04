from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase , sessionmaker

db_url = "postgresql+psycopg2://shachi:7023690737@localhost:5432/ecommerce"
engine = create_engine(db_url)

class Base(DeclarativeBase):
    pass

session = sessionmaker(autocommit = False , autoflush = False, bind = engine)
 