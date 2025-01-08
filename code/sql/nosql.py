import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client["entertainment"]
coll = db["movies"]

# CREATE
list_to_add = [
    {"title": "Star Wars", "year": 2017, "genre": ["science fiction", "adventure"]},
    {"title": "Star Wars 2", "year": 2017, "genre": ["science fiction", "adventure"]},
    {"title": "Star Wars 3", "year": 2017, "genre": ["science fiction", "adventure"]}
]
coll.insert_many(list_to_add)

# READ
sci_fi_movies = coll.find({"genre": {"$in": ["science fiction"]}})
for movie in sci_fi_movies:
    print(movie)

# UPDATE
coll.update_many(
    {"year": {"$gt": 2015}},      # Filter
    {"$set": {"genre": "action"}} # Update action
)

# DELETE
coll.delete_many({"genre": "action"})