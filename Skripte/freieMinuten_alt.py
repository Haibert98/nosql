import redis
from pymongo import MongoClient
from redisEinspeisen import HOST, DB
from datetime import timedelta, datetime

PORT=27017
NACHNAME = 0
VORNAME = 1
GEBURTSDATUM = 2
STADT = 3
GESCHLECHT = 4
FREIEMINUTEN = 5

def DBVerbindung():
    mc = MongoClient(host=HOST, port=PORT)
    mdb = mc.fahrradverleih
    rdb = redis.Redis(host=HOST, db= DB)
    return rdb , mdb.get_collection(mdb.list_collection_names()[0])

def analyze(collection, rdb: redis.Redis):
    ergListe= []
    index = 0 
    for email in rdb.scan_iter():
        email = email.decode('utf8')
        print(index)
        index += 1
        totalMinuten = 0
        fahrtenListe = collection.find({"email": email})
        for fahrt in fahrtenListe:
            start = datetime.strptime(fahrt["start"], '%Y-%m-%d %H:%M:%S')
            ende = datetime.strptime(fahrt["ende"], '%Y-%m-%d %H:%M:%S')
            tmp = ende - start
            totalMinuten += tmp.total_seconds()
        ergListe.append((email, totalMinuten/60))
    return ergListe

def execute(rdb: redis.Redis, data: list):
    with rdb.pipeline() as pipe:
        for key, minutes in data:
            pipe.rpush(key, str(round(minutes*0.05, 0)))
        pipe.execute()

def angebotAnzeigen(rdb: redis.Redis):
    for key in rdb.scan_iter():
        key = key.decode("utf8")
        with open("/home/nosql/bigdata_projekt/angebote.txt", "a") as file:
            file.write("Nutzer " + rdb.lindex(key, VORNAME).decode("utf8") + " " + rdb.lindex(key, NACHNAME).decode("utf8") + " hat " + rdb.lindex(key, FREIEMINUTEN).decode("utf8")  + " freie Minuten\n") 

if __name__ == '__main__':
    #rDB, mDB = DBVerbindung()
    #data = analyze(mDB, rDB)
    #execute(rDB, data)
    #angebotAnzeigen(rDB)
 with open("/home/nosql/bigdata_projekt/csvData/ausleihdaten.csv", "r", newline='\n') as file:
    file.readline()
    totalminuten= 0
    for row in file.readlines():
        tmp = row.rstrip().split(",")
        start = datetime.strptime(tmp[1], '%Y-%m-%d %H:%M:%S')
        ende = datetime.strptime(tmp[2], '%Y-%m-%d %H:%M:%S')
        tmp = ende - start
        totalminuten += tmp.total_seconds()