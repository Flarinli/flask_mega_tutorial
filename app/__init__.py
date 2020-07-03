from flask import Flask
from config import Config


app = Flask(__name__)  # noqa
app.config.from_object(Config)  # noqa

from app import routes
