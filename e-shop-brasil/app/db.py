from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://mongo:27017/')
    db = client['e_shop']
    return db
