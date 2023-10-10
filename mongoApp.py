import datetime

import pymongo as pyM

client = pyM.mongo_client('')

db = client.test
collection = db.test_collection
print(collection)

post = {
    "author": "Mike",
    "text": "My first mongoDb application based on Python",
    "tags": ["mongodb", "python3", "pymongo"],
    "data": datetime.datetime.now()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(posts)

new_posts = [{
    "author": "Mike",
    "text": "Another post",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.now()
},
    {
    "author": "Joao",
    "text": "Another post joao",
    "title": "mongo is fun",
    "date": datetime.datetime(2023, 11,10,10,45)
}]

result = posts.insert_many(new_posts)
print(result.inserted_ids)


for post in posts.find():
    print(post)