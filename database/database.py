import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()

db = PostgresqlDatabase(os.getenv('DATABASE_URI', ''))