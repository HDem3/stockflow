from sqlalchemy import create_engine #collegamento tra sqlalchemy e il database
from sqlalchemy.orm import sessionmaker #tipo il connect di sqlite3
from sqlalchemy.orm import declarative_base #tipo il basemodel di pydantic ma per sqlalchemy
from dotenv import load_dotenv
import os

load_dotenv() #carica le variabili d'ambiente dal file .env

DATABASE_URL = os.getenv("DATABASE_URL") #prende la variabile d'ambiente DATABASE_URL dal file .env

engine = create_engine(DATABASE_URL) #crea il collegamento tra sqlalchemy e il database

SessionLocal= sessionmaker(
    bind=engine, #collega la sessione al database
    autocommit=False, #non fa il commit automatico
    autoflush=False, #non fa il flush automatico
)

Base = declarative_base()

def get_db():
    db= SessionLocal()

    try: yield db
    finally: db.close()

