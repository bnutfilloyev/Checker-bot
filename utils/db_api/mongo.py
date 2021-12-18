from pymongo import MongoClient
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from data.config import IP

client = MongoClient(IP)
storage = MongoStorage()

database = client["checkerbot"]

users_db = database["users"]
