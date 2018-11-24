from pymongo import MongoClient
import datetime
import urllib.parse

username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('BoaVista1')


client = MongoClient()
client = MongoClient('mongodb://%s:%s@192.168.178.36:27017/test' % (username, password))

db = client['test']
collection = db.test_collection
collection = db['test-collection']

post = {"author": "Mike",
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
