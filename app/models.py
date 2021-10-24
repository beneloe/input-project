from app import app, db

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), index = True, unique = True) 
  order_id = db.Column(db.Integer,  db.ForeignKey('order.id'))
  
  def __repr__(self):
        return "{}".format(self.username)

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