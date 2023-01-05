from pymongo import MongoClient
from redisEinspeisen import HOST, DB
PORT=27017
def DBVerbindung():
    client = MongoClient(host=HOST, port=PORT)
    db = client["fahrradverleih"]
    return db

def buildPipeline():
    return [
        {
            "$group": {
                "_id": "$email",
                "freieMinuten": { "$sum": { "$round": [{"$multiply": [{ "$abs": { "$subtract": ["$ende", "$start"] } }, 1/60000*0.05] } , 0]}}
                #"difference": { "$multiply": [{ "$sum": { "$abs": { "$subtract": ["$ende", "$start"] } } }, 1/600000.05] }
            }
        },
        {
            "$project": {
                "_id":0,
                "name":"$_id",
                "freieMinuten": 1
                }
        },
        {
            "$out": {
                "db":"fahrradverleih" , 
                "coll":"results" 
                }
        }
    ]

def aggregate(db, pipeline):
    result = db.ausleihdaten.aggregate(pipeline)
    # with open("angebote.txt", "a") as file:
    #     for doc in result:
    #         file.write(str(doc) + "\n")


if __name__=='__main__':
    db = DBVerbindung()
    aggregate(db, buildPipeline())
