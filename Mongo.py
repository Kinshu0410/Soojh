from pymongo import MongoClient
import dns
str = 'mongodb+srv://Kinshu04101:Qwert123@cluster0.ckcyx.mongodb.net/test?retryWrites=true&w=majority'
client=MongoClient(str)
db=client["test"]
col=db["test1"]
print(db.list_collection_names())
print("hjjk")
