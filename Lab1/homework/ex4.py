from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1 .  Connect to database
client = MongoClient(mongo_uri)

#2 .  Get database
db = client.get_default_database()

#3 .  Count the number of customers group by refs
events_customers = db.customers.count({"ref": "events"})
ads_customers = db.customers.count({"ref": "ads"})
wom_customers = db.customers.count({"ref": "wom"})

print("Customers are acquired from Events:",events_customers,"\n\
Customers are acquired from advertisements:",ads_customers,"\n\
Customers are acquired from word of mouth:",wom_customers)

#4 .   Prepare data
labels = ["Events","Ads","Wom"]
values = [events_customers,ads_customers,wom_customers]

#5 .   Plot
pyplot.pie(values,
           labels=labels,
           autopct='%.2f%%'
)
pyplot.axis("Equal")

#6 .   Show
pyplot.show()




