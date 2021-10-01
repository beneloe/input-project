from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from helper import pets

app = Flask(__name__)

@app.route('/')
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