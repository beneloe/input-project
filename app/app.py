from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from helper import pets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'WrXjh&KsezqN4F!7JjrxKi3#cvtvYXpzW7tPk7HR3JH!WEa83SARa@xq&^Am4hAF$4ahWx&n@L59YV3Riy*jhw&2wiX#2BUTUGe$xbig58b6enZ$ZuvC$%57mcqn9xR'

db = SQLAlchemy(app)

db.create_all()

@app.route('/', methods=["GET", "POST"])
def index():
  return render_template("mainpage.html")

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

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  animal = pets[pet_type]
  pet = animal[pet_id]
  return f'''
  <h1>{pet['name']}</h1>
  <img src="{pet['url']}">
  <p>{pet['description']}</p>
  <ul>
    <li>{pet['breed']}</li>
    <li>{pet['age']}</li>
  </ul>
  '''

if __name__ == "__main__":
    app.run()

import routes