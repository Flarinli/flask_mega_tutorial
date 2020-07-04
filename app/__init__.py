from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)  # noqa
app.config.from_object(Config)  # noqa
db = SQLAlchemy(app)  # noqa
migrate = Migrate(app, db)  # noqa
login = LoginManager(app)  # noqa
login.login_view = 'login'  # noqa

from app import (routes, models)
