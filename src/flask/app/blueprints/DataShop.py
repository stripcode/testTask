from flask import Blueprint, jsonify
from app.domain import Shop
from flask_login import login_required
from app.marsh import ShopSchema



app = Blueprint("DataShop", __name__)
shopsSchema = ShopSchema(many = True)



@app.route("/")
@login_required
def getShops():
  shops = Shop.query.all()
  return jsonify(shopsSchema.dump(shops).data)