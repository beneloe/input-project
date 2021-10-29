from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), index = True, unique = False) 
  email = db.Column(db.String(120), index = True, unique = False) 
  password = db.Column(db.String(120))
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
  
  def __repr__(self):
    return "{}".format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

class Meal(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  cook = db.Column(db.String(80), index = True, unique = False)
  meal_name = db.Column(db.String(80), index = True, unique = False)
  price = db.Column(db.String(80), index = True, unique = False)
  def __repr__(self):
    return f"{self.meal_name} ({self.price}) by chef {self.cook}"

class Item(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'))
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
  def __repr__(self):
    return f"{Meal.query.get(self.meal_id).meal_name} ({Meal.query.get(self.meal_id).price}) by chef {Meal.query.get(self.meal_id).cook}"

class Order(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  items = db.relationship('Item', backref = 'orders', lazy = 'dynamic')