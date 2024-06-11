from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

SQLALCHEMY_DATABASE_URL = f"""postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"""

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# import time
# import psycopg2
# from psycopg2.extras import RealDictCursor

# while True: # Postgres database
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastAPI', user='postgres', password='1104', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was sucessfull")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(3)