from pymongo import MongoClient
import datetime
import urllib.parse

username = urllib.parse.quote_plus('user1')
password = urllib.parse.quote_plus('BoaVista1')
host = urllib.parse.quote_plus('CentOS')
port = urllib.parse.quote_plus('27017')

client = MongoClient()
client = MongoClient('mongodb://%s:%s@%s:%s/' % (username, password, host, port))

db = client['test']
collection = db.test_collection
collection = db['test-collection']

post = {"author": "Stephan",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
#print(dict(posts.find({})))
print(posts.find_one({"author": "Mike"}))


import pprint
for post in posts.find():
        pprint.pprint(post)
