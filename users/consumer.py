from kafka import KafkaConsumer
from json import loads

from database import db

from users.models import User
from users.serializers import UserSchema

consumer = KafkaConsumer(
    'demo',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='demo-group',
    #  value_deserializer=lambda x: loads(x.decode('utf-8'))
     )

# client = MongoClient('localhost:27017')
# collection = client.numtest.numtest

for message in consumer:
    message = message.value
    # collection.insert_one(message)
    print(message)

    user = User(
        firstname=message.get("firstname", ""),
        lastname=message.get("lastname", ""),
        middlename=message.get("middlename", ""),
        birthday=message.get("birthday", ""),
        address=message.get("address", ""),
    )
    db.session.add(user)
    db.session.commit()