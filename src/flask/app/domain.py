from flask import current_app
from .ext import db
from hashlib import sha1
from time import time



class User(db.Model):
  # Пользователь системы
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key = True)
  fio = db.Column(db.String(255), nullable = False)
  login = db.Column(db.String(255), nullable = False)
  passwordHash = db.Column(db.String(255), nullable = False)
  createTime = db.Column(db.Integer, nullable = False)
  updateTime = db.Column(db.Integer, nullable = False)
  is_active = True
  is_authenticated = True

  def __init__(self, fio, login, rawPassword):
    self.setFio(fio)
    self.setLogin(login)
    self.setPassword(rawPassword)
    currentTime = time()
    self.createTime = currentTime
    self.updateTime = currentTime

  def get_id(self):
    return self.id

  def setFio(self, fio):
    self.fio = fio

  def setLogin(self, login):
    self.login = login

  def setPassword(self, rawPassword):
    self.passwordHash = self.generatePasswordHash(rawPassword)

  @staticmethod
  def generatePasswordHash(password):
    password = password + current_app.config["SALT"]
    return sha1(password.encode("utf-8")).hexdigest()