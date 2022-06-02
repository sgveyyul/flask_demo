from database import db

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):
    __tablename__ = 'user'
    
    firstname = db.Column(db.String(128), nullable=False)
    lastname  = db.Column(db.String(128), nullable=False)
    middlename = db.Column(db.String(128), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"
