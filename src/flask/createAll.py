# скрипт создает необходимые таблицы и наполняет их тестовыми данными

from app import createApp
from app.ext import db
from app.domain import User, Shop, DocType, Product, Document
from random import randint

app = createApp()
app.app_context().push()
db.create_all()

users = []
shops = []
products = []

shopPattern = ["Монетка", "Пятерочка", "Связной"]
productPattern = ["Колбаса", "Сыр", "Хлеб"]

# сохздаем пользователе
for i in range(1, 100):
  user = User("Админ" + str(i), "admin" + str(i), "admin" + str(i))
  db.session.add(user)
  users.append(user)

# создаем магазины
for i in range(1, 100):
  shop = Shop("{shop} №{}".format(i, shop = shopPattern[randint(0, len(shopPattern) - 1)]))
  db.session.add(shop)
  shops.append(shop)

# создаем продукты
for i in range(1, 100):
  product = Product("{product} №{}".format(i, product = productPattern[randint(0, len(productPattern) - 1)]))
  db.session.add(product)

# создаем типы документов
docTypes = [DocType("Чек"), DocType("Расписка"), DocType("Чесное слово")]
for docType in docTypes:
  db.session.add(docType)

# создаем документы
for i in range(1, 100):
  doc = Document(shops[randint(0, len(shops) - 1)], docTypes[randint(0, len(docTypes) - 1)], users[randint(0, len(users) -1 )])
  db.session.add(doc)

db.session.commit()