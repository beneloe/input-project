from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, RadioField, BooleanField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from models import User

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])

  def validate_username(self,field):
    username = field.data
    if username == "admin":
      raise ValidationError("Invalid Username")

  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired()])
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