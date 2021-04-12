from enum import unique
from flask_sqlalchemy import SQLAlchemy
import flask_login


db = SQLAlchemy()
class Food_User(db.Model, flask_login.mixins.UserMixin):
    __tablename__ = 'Food_User' # Name of the table in our database
    # Defining the columns
    foodId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    fat = db.Column(db.Float, unique=False, nullable=False)
    prot = db.Column(db.Float, unique=False, nullable=False)
    carb = db.Column(db.Float, unique=False, nullable=False)
    callories = db.Column(db.Float, unique=False, nullable=False)
    date = db.Column(db.Date,unique=True,nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('App_User.userId'))
    def get_id(self):
        return db.text_type(self.foodId)


class App_User(db.Model, flask_login.mixins.UserMixin):
    __tablename__ = 'App_User' # Name of the table in our database
    # Defining the columns
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email=db.Column(db.String(80), unique=True,nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    mobilePhone = db.Column(db.String(80), unique=False, nullable=True)
    gender = db.Column(db.String(80), unique=True,nullable=False)
    weight = db.Column(db.Float,unique=False,nullable=False)
    height = db.Column(db.Float,unique=False,nullable=False)
    age = db.Column(db.Integer,unique=False,nullable=False)
    def get_id(self):
        return chr(self.userId)