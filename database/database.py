from dotenv import load_dotenv
from peewee import SqliteDatabase

load_dotenv()

db = SqliteDatabase('people.db')