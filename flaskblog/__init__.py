from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from flask_mail import Mail
from flaskblog.hasla_nie_wstawiac_do_git import password

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ef0b2d7f636abd0015a9bc319294362'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['DEBUG'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
# db.create_all(app)
with app.app_context():
    db.create_all()

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "szycah3@gmail.com"
app.config['MAIL_PASSWORD'] = password

mail = Mail(app)

from flaskblog import routes