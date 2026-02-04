from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()

def init_db(app):
    connect(db='curses_db', host=os.getenv('MONGO_URI'))