from flask import current_app
from .ext import db



class User(db.Model):
  # Пользователь системы
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key = True)
  fio = db.Column(db.String(255), nullable = False)
  ligin = db.Column(db.String(255), nullable = False)
  passwordHash = db.Column(db.String(255), nullable = False)
  createTime = db.Column(db.Integer, nullable = False)
  updateTime = db.Column(db.Integer, nullable = False)

  def __init__(self, fio, login, rawPassword):
    self.setFio(fio)
    self.setLogin(login)
    self.setHashFromPassword(rawPassword, current_app.config["SALT"])

  def setFio(self, fio):
    self.fio = fio

  def setLogin(self, login):
    self.login = login

  def setPasswordHash(self, password, salt):
    self.passwordHash = password + salt