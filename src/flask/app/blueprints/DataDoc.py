from flask import Blueprint, jsonify, request
from app.domain import Document
from flask_login import login_required
from app.marsh import DocumentSchema
from app.ext import db



bigQuery = "SELECT document.id, docType.name as docTypeName, shop.name as shopName, user.fio as userFio FROM document, docType, shop, user \
  WHERE document.docTypeId = docType.id and document.shopId = shop.id and document.userId = user.id \
  and (docType.name LIKE '%{phrase}%' or shop.name LIKE '%{phrase}%' or user.fio LIKE '%{phrase}%' or document.id LIKE '%{phrase}%' )"



app = Blueprint("DataDoc", __name__)
docSchema = DocumentSchema()
docsSchema = DocumentSchema(many = True, exclude = ("products",))



@app.route("/")
@login_required
def getDocs():
  docs = Document.query.order_by(Document.updateTime.asc()).all()
  return jsonify(docsSchema.dump(docs).data)


@app.route("/search/")
@login_required
def search():
  phrase = request.args.get("phrase", "")
  rows = []
  for row in db.session.execute(bigQuery.format(phrase = phrase)):
    rows.append({key: value for key, value in row.items()})
  return jsonify(rows)



@app.route("/<int:docId>")
@login_required
def getDoc(docId):
  doc = Document.query.get_or_404(docId)
  return jsonify(docSchema.dump(doc).data)