from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("mainpage.html")

if __name__ == "__main__":
    app.run()