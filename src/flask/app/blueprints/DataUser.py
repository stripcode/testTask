from flask import Blueprint, jsonify
from app.domain import User
from flask_login import login_required, current_user
from app.marsh import UserSchema



app = Blueprint("DataUser", __name__)
userSchema = UserSchema()



@app.route("/session/")
@login_required
def getUserSession():
  user = User.query.filter_by(id = current_user.id).one_or_none()
  return jsonify(userSchema.dump(user).data)