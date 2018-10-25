#fileName : db.py
#author : Aishwarya Pagalla
# last modified : 10/24/2018

import pprint
from sys_met import *
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test_database
db = client["metdb0"]
collection = db.test_collection
collection = db['metcollector']
doc = sys_met.met
		
posts = db.posts
post_id = posts.insert_one(doc).inserted_id
print(post_id)
db.collection_names(include_system_collections=False)
pprint.pprint(posts.find_one())


