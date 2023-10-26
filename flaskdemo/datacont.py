from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Data(db.Model):
    __tablename__= "Data"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(100))
    address = db.Column(db.String(100))


    def __init__(self, name, email, phone, address ):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

