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
from models import User, Meal

@app.route('/', methods=["GET", "POST"])
def index():
  meals = Meal.query.all()
  user = current_user
  return render_template("mainpage.html", meals=meals, user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
  user = current_user
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    if user and form.password.data == user.password:
      login_user(user)

      return redirect(url_for('index'))
    else:
      return render_template('login.html', form=form, user=user)
  return render_template('login.html', form=form, user=user)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  user = current_user
  form = RegistrationForm()
  if form.validate_on_submit():
    new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return redirect(url_for('index'))

  return render_template('register.html', form = form, user=user)

@app.route('/meal', methods=['GET', 'POST'])
def meal():
  user = current_user
  form = MealForm()
  if form.validate_on_submit():
    meal = Meal(meal_name=form.meal_name.data, meal_image=form.meal_image.data, cook=form.cook.data, price=form.price.data)
    db.session.add(meal)
    db.session.commit()
    return redirect(url_for('index'))
  return render_template('meal.html', form = form, user=user)

@app.route('/meal/<int:meal_id>', methods=['GET', 'POST'])
def individual_meal(meal_id):
  user = current_user
  meal = Meal.query.filter_by(id = meal_id).first()
  return render_template('individual_meal.html', meal = meal, user=user)

@app.route('/meal/all', methods=['GET', 'POST'])
def all_meals():
  user = current_user
  meals = Meal.query.all()
  return render_template('list.html', meals = meals, user=user)
