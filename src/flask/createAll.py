from app import createApp
from app.ext import db
from app.domain import User, Shop

app = createApp()
app.app_context().push()
db.create_all()

for i in range(1, 100):
  user = User("Админ" + str(i), "admin" + str(i), "admin" + str(i))
  db.session.add(user)

for i in range(1, 100):
  shop = Shop("Магазин №" + str(i))
  db.session.add(shop)

db.session.commit()