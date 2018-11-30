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
doc1 = sys_met.met
doc2 = sys_met.sett
doc3 = sys_met.inf		
postmet = db.postmet
postsett = db.postsett
postinf = db.postinf
post_id = postmet.insert_one(doc1).inserted_id
post_id = postsett.insert_one(doc2).inserted_id
post_id = postinf.insert_one(doc3).inserted_id
print(post_id)
db.collection_names(include_system_collections=False)
pprint.pprint(postmet.find_one())
pprint.pprint(postsett.find_one())
pprint.pprint(postinf.find_one())


