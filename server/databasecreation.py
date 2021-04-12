from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SERVER = 'LAPTOP-A84E5O9M\SQLEXPRESS'
DATABASE = 'callory_database'
DRIVER = 'SQL Server Native Client 11.0'
DATABASE_CONNECTION = f'mssql://{SERVER}/{DATABASE}?trusted_connection=yes&driver={DRIVER}'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

db = SQLAlchemy(app)


import flask_login


class App_User(db.Model, flask_login.mixins.UserMixin):
    __tablename__ = 'App_User' # Name of the table in our database
    # Defining the columns
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    mobilePhone = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    gender = db.Column(db.String(80),unique=True,nullable=False)
    weight = db.Column(db.Float,unique=False,nullable=False)
    height = db.Column(db.Float,unique=False,nullable=False)
    age = db.Column(db.Integer,unique=False,nullable=False)
    food_user = db.relationship("Food_User", back_populates="App_User")
    def get_id(self):
        return db.text_type(self.userId)

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
    app_user = db.relationship("App_User", back_populates="Food_User")
    def get_id(self):
        return db.text_type(self.foodId)

class UserSession(db.Model):
    __tablename__ = 'UserSession' # Name of the table in our database
    # Defining the columns
    userSessionId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    loginDate = db.Column(db.DateTime, nullable=False)
    expireDate = db.Column(db.DateTime, nullable=False)
    loggedOut = db.Column(db.Boolean, nullable=False)
    jwToken = db.Column(db.String(4000), nullable=False)
    url = db.Column(db.String(4000), nullable=True)
    logoutDate = db.Column(db.DateTime, nullable=True)



db.create_all()
db.session.commit()