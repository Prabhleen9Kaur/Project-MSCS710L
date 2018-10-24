from pymongo import MongoClient

client = MongoClient("mongodb://system_metrics:system_metrics@connections-shard-00-00-pdrg1.mongodb.net:27017,connections-shard-00-01-pdrg1.mongodb.net:27017,connections-shard-00-02-pdrg1.mongodb.net:27017/test?ssl=true&replicaSet=Connections-shard-0&authSource=admin&retryWrites=true")

print(client.Connections)