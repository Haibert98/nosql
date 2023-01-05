import os
import random
from datetime import timedelta, datetime

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    tmp = str(start + timedelta(seconds=random_second)).split(" ")
    return tmp[0]

geschlecht = ["w", "m", "d"]

startDatum = datetime.strptime('1/1/1950', '%m/%d/%Y')
endDatum = datetime.strptime('1/1/2008', '%m/%d/%Y')


nameF = open("../csvData/nachnamen.csv", "r", encoding="utf8")
vornameF = open("../csvData/vornamen.csv", "r", encoding="utf8")
stadtF = open("../csvData/stadt.csv", "r", encoding="utf8")

vornamen = vornameF.read().splitlines()
nachnamen = nameF.read().splitlines()
stadt = stadtF.read().splitlines()
email = []
for i in range(len(vornamen)):
    email.append(vornamen[i].lower() + "." + nachnamen[i].lower() + str(i) +"@test.com")

with open("../csvData/daten.csv", "w+", encoding="utf8") as output:
    output.write("email, nachname, vorname, geburtsdatum, stadt, geschlecht\n")
    for i in range(len(vornamen)):
        pass
        output.write(email[i]+ ","+ nachnamen[i] + "," + vornamen[i] + "," + random_date(startDatum, endDatum) + "," + stadt[random.randint(0, len(stadt)-1)] + "," + geschlecht[random.randint(0, 2)])
        output.write("\n")


