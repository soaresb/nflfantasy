import pymongo
import ssl
import os

client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"), ssl_cert_reqs=ssl.CERT_NONE)

if client:
    database = client.get_default_database()
