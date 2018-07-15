from flask import Flask
from flask_login import LoginManager
from .ext import db
from .domain import User



def createApp():
  app = Flask(__name__)
  app.config.from_pyfile("config.default.py")
  app.config.from_envvar("TEST_TASK_PRODUCTION", silent = True)
  db.init_app(app)


  # настройка аутентификации
  login_manager = LoginManager()
  login_manager.init_app(app)
  login_manager.login_view = "Pages.defaultPage"

  @login_manager.user_loader
  def load_user(userId):
    if userId:
      user = User.query.filter_by(id = userId).one_or_none()
      return user
    return None


  from .blueprints.Pages import app as Pages
  from .blueprints.DataAuthRequest import app as DataAuthRequest
  from .blueprints.DataUser import app as DataUser

  app.register_blueprint(Pages)
  app.register_blueprint(DataAuthRequest, url_prefix = "/data/authRequest")
  app.register_blueprint(DataUser, url_prefix = "/data/user")


  return app