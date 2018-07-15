from app import createApp
from app.ext import db
from app.domain import User

app = createApp()
app.app_context().push()
db.create_all()

for i in range(1, 10):
  user = User("Админ" + str(i), "admin" + str(i), "admin" + str(i))
  db.session.add(user)

db.session.commit()