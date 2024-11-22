from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mssql+pyodbc://@localhost/NoviBank?driver=ODBC Driver 17 for SQL Server&trusted_connection=yes")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_context():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()