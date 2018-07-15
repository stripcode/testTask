from flask import Blueprint, send_file, current_app
from flask_login import login_required
from barcode.writer import ImageWriter
import barcode
import os



app = Blueprint("DataProduct", __name__)
code128 = barcode.get_barcode_class('code128')



@app.route("/<int:productId>/barcode/")
@login_required
def getBarcode(productId):
  c = code128(str(productId), writer = ImageWriter())
  filename = os.path.join(current_app.config["BARCODES"], "{}.png".format(productId))
  with open(filename, "wb") as file:
    c.write(file)
    return send_file(filename)
  return "barcode_not_found", 404