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

  is_active = True # аттрибут нужен для flask_login
  is_authenticated = True # аттрибут нужен для flask_login

  def __init__(self, fio, login, rawPassword):
    self.setPassword(rawPassword)
    self.fio = fio
    self.login = login
    currentTime = time()
    self.createTime = currentTime
    self.updateTime = currentTime

  def get_id(self):
    # метод нужен для flask_login
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



class Shop(db.Model):
  # Магазин
  __tablename__ = "shop"
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255), nullable = False)
  createTime = db.Column(db.Integer, nullable = False)
  updateTime = db.Column(db.Integer, nullable = False)

  def __init__(self, name):
    self.name = name
    currentTime = time()
    self.createTime = currentTime
    self.updateTime = currentTime




class Product(db.Model):
  # Товар
  __tablename__ = "product"
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255), nullable = False)
  createTime = db.Column(db.Integer, nullable = False)
  updateTime = db.Column(db.Integer, nullable = False)

  def __init__(self, name):
    self.name = name
    currentTime = time()
    self.createTime = currentTime
    self.updateTime = currentTime



class DocType(db.Model):
  # Тип документа
  __tablename__ = "docType"
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255), nullable = False)
  createTime = db.Column(db.Integer, nullable = False)
  updateTime = db.Column(db.Integer, nullable = False)

  def __init__(self, name):
    self.name = name
    currentTime = time()
    self.createTime = currentTime
    self.updateTime = currentTime



class Document(db.Model):
  # Документ
  __tablename__ = "document"
  id = db.Column(db.Integer, primary_key = True)
  createTime = db.Column(db.Integer, nullable = False)
  updateTime = db.Column(db.Integer, nullable = False)

  # привязка магазина
  shopId = db.Column(db.Integer, db.ForeignKey('shop.id'))
  shop = db.relationship("Shop")

  # привязка типа документа
  docTypeId = db.Column(db.Integer, db.ForeignKey('docType.id'))
  docType = db.relationship("DocType")

  # привязка типа документа
  userId = db.Column(db.Integer, db.ForeignKey('user.id'))
  user = db.relationship("User")

  def __init__(self, shop, docType, user):
    self.shop = shop
    self.docType = docType
    self.user = user
    currentTime = time()
    self.createTime = currentTime
    self.updateTime = currentTime