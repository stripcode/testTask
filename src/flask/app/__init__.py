from flask import Flask
from .ext import db



def createApp():
  app = Flask(__name__)
  app.config.from_pyfile("config.default.py")
  app.config.from_envvar("TEST_TASK_PRODUCTION", silent = True)
  db.init_app(app)
  return app