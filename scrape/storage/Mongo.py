import pymongo
from pymongo import UpdateOne
import ssl
import os

class Mongo(object):
    def __init__(self):
        super().__init__()
        self.database = None
        self.client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"), ssl_cert_reqs=ssl.CERT_NONE)
        if self.client:
            self.database = self.client.get_default_database()
    
    def fetch_one(self, collection, query, projection=None):
        if projection:
            return self.database[collection].find_one(query, projection)
        else:
            return self.database[collection].find_one(query)
    
    def update_player(self, player):
        _set = {k: v for k, v in player.__dict__.items() if v is not None}
        return UpdateOne({"_id": player.id}, {"$set": _set })
    
    def bulk_update(self, to_update, collection):
        cmds = list()
        for i in to_update:
            cmds.append(i)
        resp = self.database[collection].bulk_write(cmds)
        return resp

