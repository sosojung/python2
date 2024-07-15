import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("scret.json")
firebase_admin.initialize_app(cred)
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference('key', url='https://qqqq-24936-default-rtdb.firebaseio.com/')
ref.update({"hsssi": 1234})
print(ref.get())