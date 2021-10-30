from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from helper import pets

app = Flask(__name__)

app.config['SECRET_KEY'] = 'WrXjh&KsezqN4F!7JjrxKi3#cvtvYXpzW7tPk7HR3JH!WEa83SARa@xq&^Am4hAF$4ahWx&n@L59YV3Riy*jhw&2wiX#2BUTUGe$xbig58b6enZ$ZuvC$%57mcqn9xR'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
import routes
from models import User
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
  return User.query.get(id)

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'''
  <h1>List of {pet_type}</h1>
  <ul>
  '''
  for idx, animal in enumerate(pets[pet_type]):
    html += f'''<li><a href='/animals/{pet_type}/{idx}'>{animal['name']}</a></li>'''
  html += '</ul>'
  return html

if __name__ == "__main__":
    app.run()

