from kafka import KafkaConsumer
from json import loads

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

class User(Base):
    __tablename__ = 'user'
    
    firstname = db.Column(db.String(128), nullable=False)
    lastname  = db.Column(db.String(128), nullable=False)
    middlename = db.Column(db.String(128), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

    

if __name__=='__main__':
    consumer = KafkaConsumer(
        'demo',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='demo-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

    # client = MongoClient('localhost:27017')
    # collection = client.numtest.numtest

    for message in consumer:
        message = message.value
        # collection.insert_one(message)

        user = User(
            firstname=message.get("firstname", ""),
            lastname=message.get("lastname", ""),
            middlename=message.get("middlename", ""),
            birthday=message.get("birthday", ""),
            address=message.get("address", ""),
        )
        db.session.add(user)
        db.session.commit()