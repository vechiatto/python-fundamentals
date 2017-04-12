#import mongo client

from pymongo import MongoClient

#connect

client = MongoClient('127.0.0.1')
db = client['devops']

#insert

db.fila.insert ({
	"_id": 4,
	"servico": "local_intra",
	"status": 0
})

#update

db.fila.update(
	{"_id": 2, "servico": "internet"},
	{"$set": {"status": 6}}
)

#delete
db.fila.remove({"_id": 1})

#find

for d in db.fila.find({}):
	print d