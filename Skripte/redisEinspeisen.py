import redis
import csv
HOST = "localhost"
DB = 1
EMAIL = 0
NACHNAME = 1
VORNAME = 2
GEBURTSDATUM = 3
STADT = 4
GESCHLECHT = 5
FREIEMINUTEN = 6
def datenEinlesen(file, db):
    cnt = 0
    with db.pipeline() as pipe:
        with open(file, newline='\n') as csvFile:
            #data = csv.DictReader(csvFile, delimiter=',', skipinitialspace=True)
            # for e, nachname, vorname, gd, stadt, ge in data:
            csvFile.readline()
            for row in csvFile.readlines():
                cnt += 1
                tmp = row.rstrip().split(",")
                pipe.rpush(tmp[EMAIL],  str(tmp[NACHNAME]),  str(tmp[VORNAME]),
                        str(tmp[GEBURTSDATUM]),  str(tmp[STADT]), str(tmp[GESCHLECHT] ))
                if cnt % 100 == 0 :
                    pipe.execute()
                    cnt = 0
            pipe.execute()


def DBVerbindung():
    db = redis.Redis(host=HOST, db= DB)
    db.flushdb()
    return db



if __name__ == "__main__":
    r = DBVerbindung()
    file = "/home/nosql/bigdata_projekt/csvData/daten.csv"
    
    datenEinlesen(file, r)
