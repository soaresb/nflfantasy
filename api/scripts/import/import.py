import pymongo
import ssl
import os
import sys
import getopt
import json
import re
from pymongo import UpdateOne

def main(args):
    try:
        opts, args = getopt.getopt(args, None, ["filename="])
    except getopt.GetoptError:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        sys.exit(2)
    filename = None
    for opt, arg in opts:
        if opt == '--help':
            sys.exit()
        elif opt in '--filename':
            filename = arg

    # client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"), ssl_cert_reqs=ssl.CERT_NONE)
    # if client:
    #     database = client.get_default_database()
    
    # players = database.players
    data = process_file(filename)


def camel_to_snake(val):
  name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', val)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', val).lower()    


def add_players(data):
    ops = list()
    client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"), ssl_cert_reqs=ssl.CERT_NONE)
    if client:
        database = client.get_database("players")
    players_collection = database.players

    for player in data:
        cleaned = {}
        for key, value in player.items():
            cleaned[camel_to_snake(key)] = value

        ops.append(UpdateOne({"_id": cleaned["player_id"]}, {"$set": cleaned}, upsert=True))
    result = players_collection.bulk_write(ops)
    


def process_file(filename):
    with open(filename, "r") as infile:
        data = json.load(infile)
        add_players(data)
        return



if __name__ == '__main__':
    main(sys.argv[1:])