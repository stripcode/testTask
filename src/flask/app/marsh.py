from marshmallow_sqlalchemy import ModelSchema
import app.domain as domain



class UserSchema(ModelSchema):
  class Meta:
    model = domain.User
    exclude = ("passwordHash",)



class ShopSchema(ModelSchema):
  class Meta:
    model = domain.Shop