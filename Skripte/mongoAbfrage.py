from pymongo import MongoClient


HOST= "localhost"
PORT= 27017

def DBVerdindung():
    mc = MongoClient(host=HOST, port=PORT)
    db = mc.fahrradverleih
    return db.get_collection(db.list_collection_names()[0])

def getDatensatz(collection, email):
    liste= []
    erg = collection.find({"email": email})
    for x in erg:
        liste.append(x["start"] + " " +x["ende"])
    return liste[0]

if __name__ == "__main__":
    collection = DBVerdindung()
    print(getDatensatz(collection, "sergey.joost10649@test.com"))
    print(getDatensatz(collection, "henri.horst799@test.com"))