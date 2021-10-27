from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, RadioField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')

class MealForm(FlaskForm):
  meal_name = StringField(label = "Meal name", validators=[DataRequired()])
  cook = StringField(label = "Cook", validators=[DataRequired()])
  price = StringField(label = "Price", validators=[DataRequired()])
  submit = SubmitField("Add meal")

def exists(item, order):
  for i in order:
    if i.meal_id == item.meal_id:
       return True
  return False