from flask import Flask

app = Flask(__name__)  # noqa

from app import routes
