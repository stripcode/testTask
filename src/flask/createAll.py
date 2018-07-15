from app import createApp
from app.ext import db
from app.domain import User, Shop, DocType, Product

app = createApp()
app.app_context().push()
db.create_all()

for i in range(1, 100):
  user = User("Админ" + str(i), "admin" + str(i), "admin" + str(i))
  db.session.add(user)

for i in range(1, 100):
  shop = Shop("Магазин №" + str(i))
  db.session.add(shop)

for i in range(1, 100):
  shop = Product("Продукт" + str(i))
  db.session.add(shop)

db.session.add(DocType("Чек"))
db.session.add(DocType("Расписка"))
db.session.add(DocType("Чесное слово"))

db.session.commit()