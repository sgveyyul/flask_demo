from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "firstname",
            "lastname",
            "middlename",
            "birthday",
            "address"
        )