from app import createApp
from app.ext import db
from app.domain import User, Shop, DocType, Product

app = createApp()
app.app_context().push()
db.create_all()

for i in range(1, 100):
  user = User("Админ" + str(i), "admin" + str(i), "admin" + str(i))
  db.session.add(user)

shopPattern = ["Монетка", "Пятерочка", "Связной"]

for i in range(1, 100):
  name = shopPattern.pop(0)
  shop = Shop("{shop} №{}".format(i, shop = name))
  db.session.add(shop)
  shopPattern.append(name)

productPattern = ["Колбаса", "Сыр", "Хлеб"]

for i in range(1, 100):
  name = productPattern.pop(0)
  shop = Product("{product} №{}".format(i, product = name))
  db.session.add(shop)
  productPattern.append(name)

db.session.add(DocType("Чек"))
db.session.add(DocType("Расписка"))
db.session.add(DocType("Чесное слово"))

db.session.commit()