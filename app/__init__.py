from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  # noqa
app.config.from_object(Config)  # noqa
db = SQLAlchemy(app)  # noqa
migrate = Migrate(app, db)  # noqa

from app import (routes, models)
