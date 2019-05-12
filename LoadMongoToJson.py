import Load_data as LD
from pymongo import MongoClient
import datetime
import time
import urllib.parse
import os
import json
import pprint


def loadmongotojson():
        # Parameter
        ################################################################################################################
        path = "C:\\Users\\Stephan\\Google Drive\\BoaVista\\json_file.json"

        username = urllib.parse.quote_plus('user1')
        password = urllib.parse.quote_plus('BoaVista1')
        host = urllib.parse.quote_plus('CentOS')
        port = urllib.parse.quote_plus('27017')
        db = 'test'
        collection = 'Kunden2'

        # MongoDB client definieren
        ################################################################################################################
        # post = {"author": "Stephan",
        #         "text": "My first blog post!",
        #         "tags": ["mongodb", "python", "pymongo"],
        #         "date": datetime.datetime.utcnow()}

        client = MongoClient()
        client = MongoClient('mongodb://%s:%s@%s:%s/' % (username, password, host, port))

        # client[db][collection].insert_many(data)

        # for i, entry in enumerate(data):
        #     client[db][collection].insert_one(entry)

        # Find and Print
        ################################################################################################################
        #
        data = []
        for post in client[db][collection].find():
                data.append(post)

        return data
        ################################################################################################################
