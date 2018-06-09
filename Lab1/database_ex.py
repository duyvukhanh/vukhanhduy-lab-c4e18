from pymongo import MongoClient

mongo_uri = "mongodb://duy-clone1:khjcon9x@ds015730.mlab.com:15730/duyc4e18-lab"

#1 .  Connect to database
client = MongoClient(mongo_uri)

#2 .  Get database
db = client.get_default_database()

#3 .  Create collection
games = db['games']
movies = db['movies']

#4 .  Create document
# new_game = {
#     "title" : "PES",
#     "description" : "Pro Evolution Soccer"
# }
new_movie = {
    "Title" : "5 Anh Em Sieu Nhan",
    "Category" : "Phim Hanh Dong Manh"
}

new1_mv = {
    "Title" : "Kim binh mai",
    "Category" : "Co trang"
}
#5 .  Insert document into collection
# movies.insert_one(new_movie)



all_game = games.find()
for game in all_game:
    print(game)