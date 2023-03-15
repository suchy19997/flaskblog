from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SECRET_KEY'] = '9ef0b2d7f636abd0015a9bc319294362'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['DEBUG'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# db.create_all(app)
with app.app_context():
    db.create_all()

from flaskblog import routes