import datetime

import pymongo as pyM

client = pyM.mongo_client('')

db =client.test
posts = db.posts

for post in posts.find():
    print(post)

print(posts.count_documents({}))
print(posts.count_documents({"author": "Mike"}))
print(posts.count_documents({"tags": "insert"}))

print(posts.find_one({"tags": "insert"}))

for post in posts.find({}).sort("date"):
    print(post)

result = db.profiles.create_index([('author', pyM.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Joao'},
]

result = db.profile_user.insert_many(user_profile_user)

print(db.list_collection_names)

collections = db.list_collection_names()

for x in collections:
    print(x)
    db[x].drop()



