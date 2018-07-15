from flask import Blueprint, request, jsonify
from app.domain import User
from flask_login import login_user



app = Blueprint("DataAuthRequest", __name__)



@app.route("/", methods = ["post"])
def processLoginForm():
  args = request.get_json()
  user = User.query.filter_by(login = args["login"], passwordHash = User.generatePasswordHash(args["password"])).one_or_none()
  if user:
    login_user(user)

  return jsonify(args)