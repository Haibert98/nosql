import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["fahrradverleih"]

# Define the map function
def map_function():
    def map_function(doc):
        yield doc["name"], 1

# Define the reduce function
def reduce_function(key, values):
    return sum(values)

# Build the pipeline
pipeline = [
    {
        "$group": {
            "_id": "$email",
            "difference": { "$sum": { "$round": [{"$multiply": [{ "$abs": { "$subtract": ["$ende", "$start"] } }, 1/60000*0.05] } , 0]}}
            #"difference": { "$multiply": [{ "$sum": { "$abs": { "$subtract": ["$ende", "$start"] } } }, 1/600000.05] }
        }
    }
]

# Perform the aggregation
result = db.ausleihdaten.aggregate(pipeline)
with open("angebote2.txt", "a") as file:
    for doc in result:
        file.write(str(doc) + "\n")

# Print the results
#counter = 0
#for doc in result:
#    print(str(counter) + " " + str(doc))
#    counter += 1