from app import db
from models import Meal, Order, Item, User

o1 = Order(id = 1)
o2 = Order(id = 2)
o3 = Order(id = 3)
o4 = Order(id = 4)

u1 = User(id = 1, username = "hungry@user.com", order_id = o1.id)
u2 = User(id = 2, username = "hungry2@user.com", order_id = o2.id)
u3 = User(id = 3, username = "hungry3@user.com", order_id = o3.id)
u4 = User(id = 4, username = "hungry4@user.com", order_id = o4.id)

m1 = Meal(id = 1, cook = "Tami", meal_name = "Healthy Salad Bowl", price = "10.50")
m2 = Meal(id = 2, cook = "Manni", meal_name = "Vegan Delight", price = "11.50")
m3 = Meal(id = 3, cook = "Joni", meal_name = "Mezze on the Go", price = "12.50")
m4 = Meal(id = 4, cook = "Lori", meal_name = "Fresh Tacos", price = "12.50") 
m5 = Meal(id = 5, cook = "Toni", meal_name = "Doshirag's Best", price = "14.50")

db.session.add(o1)
db.session.add(o2)
db.session.add(o3)
db.session.add(o4)
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.add(m1)
db.session.add(m2)
db.session.add(m3)
db.session.add(m4)
db.session.add(m5)
db.session.commit()