from faker import Faker
from pymongo import MongoClient

fake = Faker()
client = MongoClient("mongodb://localhost:27017/")
db = client["eshop"]
collection = db["clientes"]

batch = []
for _ in range(1000000):
    batch.append({"nome": fake.name(), "email": fake.email()})
    if len(batch) >= 10000:
        collection.insert_many(batch)
        batch = []

if batch:
    collection.insert_many(batch)

print("Inserção concluída.")