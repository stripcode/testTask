from flask import current_app
from .ext import db
from hashlib import sha1
from time import time


document2productRelationship = db.Table('document2product',
    db.Column('documentId', db.Integer, db.ForeignKey('document.id')),
    db.Column('productId', db.Integer, db.ForeignKey('product.id'))
)


class User(db.Model):
  # Пользователь системы
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key = True)
  fio = db.Column(db.String(255), nullable = False)
  login = db.Column(db.String(255), nullable = False, unique = True)
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
  name = db.Column(db.String(255), nullable = False, unique = True)
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
  name = db.Column(db.String(255), nullable = False, unique = True)
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
  name = db.Column(db.String(255), nullable = False, unique = True)
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
  shopId = db.Column(db.Integer, db.ForeignKey('shop.id'), index = True)
  shop = db.relationship("Shop")

  # привязка типа документа
  docTypeId = db.Column(db.Integer, db.ForeignKey('docType.id'), index = True)
  docType = db.relationship("DocType")

  # привязка типа документа
  userId = db.Column(db.Integer, db.ForeignKey('user.id'), index = True)
  user = db.relationship("User")

  products = db.relationship("Product", secondary = document2productRelationship, lazy = "dynamic")

  def __init__(self, shop, docType, user):
    self.shop = shop
    self.docType = docType
    self.user = user
    currentTime = time()
    self.createTime = currentTime
    self.updateTime = currentTime

  def addProduct(self, product):
    self.products.append(product)