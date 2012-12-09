from pymongo import Connection
from pymongo.database import Database
from pymongo.collection import Collection

############################################################################

HOST = 'localhost'
PORT = 27017
DB = 'cspan'
COLLECTION = 'house_hearings'

############################################################################

class MongoConnection:

    def __init__(self):
        self.__connection = Connection(HOST, PORT)

    def __db(self):
        return Database(self.__connection, DB)

    def __collection(self):
        return Collection(self.__db(), COLLECTION)

    def query_collection(self, limit=2707):
        return self.__collection().find(timeout=False).limit(limit)
