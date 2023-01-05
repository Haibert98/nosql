import random
from datetime import timedelta, datetime
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    tmp = start + timedelta(seconds=random_second)
    return tmp, tmp + timedelta(seconds=random.randint(60, 3600))

startDatum = datetime.strptime('4/1/2022', '%m/%d/%Y')
endDatum = datetime.strptime('4/30/2022', '%m/%d/%Y')

datenF = open("../csvData/daten.csv", "r", encoding="utf8")

daten = datenF.read().splitlines()

liste = []
for person in daten[1:]:
    for i in range(random.randint(1, 50)):
        email = person.split(",")[0]
        datum = random_date(startDatum, endDatum)
        liste.append(email + "," + str(datum[0]) + "," + str(datum[1]) + "\n")





with open("../csvData/ausleihdaten.csv", "w+", encoding="utf8") as f:
    f.write("email,start,ende\n")
    for eintrag in liste:
        f.write(eintrag)

