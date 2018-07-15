from flask import Blueprint, jsonify
from app.domain import Document
from flask_login import login_required
from app.marsh import DocumentSchema



app = Blueprint("DataDoc", __name__)
docSchema = DocumentSchema()
docsSchema = DocumentSchema(many = True, exclude = ("products",))



@app.route("/")
@login_required
def getDocs():
  docs = Document.query.order_by(Document.updateTime.asc()).all()
  return jsonify(docsSchema.dump(docs).data)



@app.route("/<int:docId>")
@login_required
def getDoc(docId):
  doc = Document.query.get_or_404(docId)
  return jsonify(docSchema.dump(doc).data)