from kafka import KafkaConsumer
from json import loads

from flask_sqlalchemy import SQLAlchemy

import sqlalchemy as db

from datetime import datetime

engine = db.create_engine("postgresql://postgres:password@localhost:5432/flask_demo")
connection = engine.connect()
metadata = db.MetaData()

_user = db.Table('user', metadata,
               db.Column('firstname', db.String(255)),
               db.Column('lastname', db.String(255)),
               db.Column('middlename', db.String(255)),
               db.Column('birthday', db.String(255)),
               db.Column('address', db.String(255)),
               db.Column('date_created', db.String(255)),
               db.Column('date_modified', db.String(255))
    )

if __name__=="__main__":

    consumer = KafkaConsumer(
        'demo',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='demo-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

    for message in consumer:
        message = message.value
        query = db.insert(_user).values(
            firstname=message.get("firstname", ""),
            lastname=message.get("lastname", ""),
            middlename=message.get("middlename", ""),
            birthday=message.get("birthday", ""),
            address=message.get("address", ""),
            date_created=datetime.now(),
            date_modified=datetime.now()
        ) 
        ResultProxy = connection.execute(query)
