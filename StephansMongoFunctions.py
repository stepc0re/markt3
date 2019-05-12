import Load_data as LD
from pymongo import MongoClient
import datetime
import time
import urllib.parse
import os
import json
import pprint


def setmongoclient():
    # Parameter setzen
    username = urllib.parse.quote_plus('user1')
    password = urllib.parse.quote_plus('BoaVista1')
    host = urllib.parse.quote_plus('CentOS')
    port = urllib.parse.quote_plus('27017')

    # MongoDB client definieren
    ################################################################################################################
    # post = {"author": "Stephan",
    #         "text": "My first blog post!",
    #         "tags": ["mongodb", "python", "pymongo"],
    #         "date": datetime.datetime.utcnow()}

    client = MongoClient()
    client = MongoClient('mongodb://%s:%s@%s:%s/' % (username, password, host, port))
    return client


def loadmongotojson(database, collection):
    # ganze collection in json schreiben
    client = setmongoclient()
    data = []
    for post in client[database][collection].find():
            data.append(post)

    return data


def loadjsontomongo(database, collection, data):
    client = setmongoclient()
    client[database][collection].insert_many(data)
