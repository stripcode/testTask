from flask import Blueprint, jsonify, request
from app.domain import Shop
from flask_login import login_required
from app.marsh import ShopSchema



app = Blueprint("DataShop", __name__)
shopsSchema = ShopSchema(many = True)



@app.route("/")
@login_required
def getShops():
  shops = Shop.query.order_by(Shop.name.asc()).all()
  return jsonify(shopsSchema.dump(shops).data)



@app.route("/search/")
@login_required
def search():
  phrase = request.args.get("phrase", "")
  shops = Shop.query.filter(Shop.name.like("%{}%".format(phrase))).order_by(Shop.name.asc()).all()
  return jsonify(shopsSchema.dump(shops).data)