from flask import Blueprint, jsonify
from app.domain import Document
from flask_login import login_required
from app.marsh import DocumentSchema



app = Blueprint("DataDoc", __name__)
docsSchema = DocumentSchema(many = True)



@app.route("/")
@login_required
def getDocs():
  docs = Document.query.order_by(Document.updateTime.asc()).all()
  return jsonify(docsSchema.dump(docs).data)