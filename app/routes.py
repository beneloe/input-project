from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from app import app, db, LoginManager
from forms import RegistrationForm, LoginForm, MealForm
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from models import User, Meal, Item, Order

@app.route('/', methods=["GET", "POST"])
def index():
  return render_template("mainpage.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    if user and form.password.data == user.password:
      login_user(user)
      return redirect(url_for('index'))
    else:
      return render_template('login.html', form=form)
  return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()

    login_user(user)

    return redirect(url_for('index'))

  return render_template('register.html', form = form)

@app.route('/profiles')
def profiles():
    current_users = User.query.all()
    return render_template('users.html', current_users = current_users)

@app.route('/profile/<int:user_id>')
def profile(user_id):
   user = User.query.filter_by(id = user_id).first_or_404(description = "No such user found.")
   meals = Meal.query.all()
   my_order = Order.query.get(user.order_id)
   return render_template('profile.html', user = user, meals = meals, my_order = my_order)

@app.route('/add_item/<int:user_id>/<int:meal_id>/<int:order_id>')
def add_item(user_id, meal_id, order_id):
   new_item = Item(meal_id = meal_id, order_id = order_id)
   user = User.query.filter_by(id = user_id).first_or_404(description = "No such user found.")
   my_order = Order.query.get(user.order_id)
   if not exists(new_item, my_order.items):
      meal = Meal.query.get(meal_id)
     
      db.session.add(new_item)
      db.session.commit()
   return redirect(url_for('profile', user_id = user_id))

@app.route('/remove_item/<int:user_id>/<int:item_id>')
def remove_item(user_id, item_id):
  
   object_to_remove = Item.query.get(item_id)
  
   db.session.delete(object_to_remove)
  
   db.session.commit()
   return redirect(url_for('profile', user_id = user_id))
   
@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
  form = MealForm()
  if request.method == 'POST' and form.validate():
    new_meal = None
   
    new_meal = Meal(meal_name = form.meal_name.data, cook = form.cook.data, price = form.price.data)
   
    db.session.add(new_meal)
   
    db.session.commit()
  else:
        flash(form.errors)
  popular_meals = Meal.query.order_by(-Meal.n)
  meals = Meal.query.all()
  return render_template('dashboard.html', meals = meals, popular_meals = popular_meals, form = form)
