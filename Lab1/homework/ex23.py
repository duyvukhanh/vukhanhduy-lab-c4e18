from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1 .  Connect to database
client = MongoClient(mongo_uri)

#2 .  Get database
db = client.get_default_database()

#3 .  Create collection
posts = db['posts']

#4 .  Create document
new_quote = {
    "title" : "5 Điều Bác Hồ dạy",
    "author" : "Khánh Duy",
    "content" : "1. Yêu Tổ quốc, yêu đồng bào. \
                 2. Học tập tốt, lao động tốt. \
                 3. Đoàn kết tốt, kỷ luật tốt. \
                 4. Giữ gìn vệ sinh thật tốt. \
                 5. Khiêm tốn, thật thà, dũng cảm."
}

#5 .  Insert document into collection
posts.insert_one(new_quote)
