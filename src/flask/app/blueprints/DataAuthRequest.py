from flask import Blueprint, request, jsonify
from app.domain import User
from app.marsh import UserSchema
from flask_login import login_user, logout_user



app = Blueprint("DataAuthRequest", __name__)
userSchema = UserSchema()



@app.route("/", methods = ["post"])
def processLoginForm():
  args = request.get_json()
  user = User.query.filter_by(login = args["login"], passwordHash = User.generatePasswordHash(args["password"])).one_or_none()
  if user:
    login_user(user)
    return jsonify(userSchema.dump(user).data)
  return "user_not_found", 404



@app.route("/logout/", methods = ["post"])
def logout():
  logout_user()
  return jsonify({})