from app import createApp
from app.ext import db

app = createApp()
app.app_context().push()
db.drop_all()