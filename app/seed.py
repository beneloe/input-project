from app import db
from models import Meal, User

u1 = User(id = 1,  username = "hungry1", email = "hungry@user.com", password = "test")
u2 = User(id = 2,  username = "hungry2", email = "hungry2@user.com", password = "test")
u3 = User(id = 3,  username = "hungry3", email = "hungry3@user.com", password = "test")
u4 = User(id = 4,  username = "hungry4", email = "hungry4@user.com", password = "test")
u5 = User(id = 5,  username = "admin", email = "admin@admin.com", password = "admin")

m1 = Meal(id = 1, cook = "Tami", meal_name = "Healthy Salad Bowl", meal_image = "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1160&q=80", price = "10.50")
m2 = Meal(id = 2, cook = "Manni", meal_name = "Vegan Delight", meal_image = "https://images.unsplash.com/photo-1541014741259-de529411b96a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1374&q=80", price = "11.50")
m3 = Meal(id = 3, cook = "Joni", meal_name = "Mezze on the Go", meal_image = "https://images.unsplash.com/photo-1543340713-1bf56d3d1b68?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1434&q=80", price = "12.50")
m4 = Meal(id = 4, cook = "Lori", meal_name = "Fresh Tacos", meal_image = "https://images.unsplash.com/photo-1611250188496-e966043a0629?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1325&q=80", price = "12.50") 
m5 = Meal(id = 5, cook = "Toni", meal_name = "Doshirag's Best", meal_image = "https://images.unsplash.com/photo-1541832676-9b763b0239ab?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1320&q=80", price = "14.50")

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.add(u5)
db.session.add(m1)
db.session.add(m2)
db.session.add(m3)
db.session.add(m4)
db.session.add(m5)
db.session.commit()