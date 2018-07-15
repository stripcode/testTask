from flask import Blueprint, render_template



app = Blueprint("Pages", __name__)

@app.route("/")
def defaultPage():
  return render_template("defaultPage.tpl")