from pymongo import MongoClient
import os

db = MongoClient(os.environ.get('LINK')).HelloBot  # Подключение к БД
collection = db.users  # Подключение к коллекции users


def add_user(user_id, first_name):
    global collection
    user_id = int(user_id)

    if collection.find_one({'user_id': user_id}) is None:
        collection.insert_one({'first_name': first_name, 'user_id': user_id})
        return True
    else:
        return False


def get_users():
    return collection.find()
