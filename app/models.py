from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), index = True, unique = False) 
  email = db.Column(db.String(120), index = True, unique = True) 
  password = db.Column(db.String(120))
  
  def __repr__(self):
    return "{}".format(self.username)

class Meal(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  cook = db.Column(db.String(80), index = True, unique = False)
  meal_name = db.Column(db.String(80), index = True, unique = False)
  meal_image = db.Column(db.String(1000), index = True, unique = False)
  price = db.Column(db.String(80), index = True, unique = False)
  def __repr__(self):
    return f"{self.meal_name} ({self.price}) by chef {self.cook}"