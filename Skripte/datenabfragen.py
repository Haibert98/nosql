import redis
from redisEinspeisen import HOST, DB

def getDatenSatz(db: redis.Redis, key):
    return db.lindex(key, 0).decode("utf8") + " " + db.lindex(key, 1).decode("utf8")


def DBVerbindung():
    db = redis.Redis(host=HOST, db= DB)
    return db

if __name__ == "__main__":
    r = DBVerbindung()
    print(getDatenSatz(r, "eunice.lenni3518@test.com"))
    # print(getDatenSatz(r, "sergey.joost10649@test.com"))