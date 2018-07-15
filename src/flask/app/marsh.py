from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import app.domain as domain



class UserSchema(ModelSchema):
  class Meta:
    model = domain.User
    exclude = ("passwordHash",)



class ShopSchema(ModelSchema):
  class Meta:
    model = domain.Shop



class DocTypeSchema(ModelSchema):
  class Meta:
    model = domain.DocType



class ProductSchema(ModelSchema):
  class Meta:
    model = domain.Product



class DocumentSchema(ModelSchema):
  shop = fields.Nested("ShopSchema", only = ("id", "name"))
  docType = fields.Nested("DocTypeSchema", only = ("id", "name"))
  user = fields.Nested("UserSchema", only = ("id", "fio"))
  products = fields.Nested("ProductSchema", many = True, only = ("id", "name"))
  class Meta:
    model = domain.Document