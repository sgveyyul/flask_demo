import json

from flask import Blueprint, request, jsonify

from database import db

from users.models import User
from users.serializers import UserSchema

from faker import Faker

users_router = Blueprint('users', __name__, url_prefix='/users')

@users_router.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    id = request.args.get('id') 
    if request.method == 'GET':
        if id:
            user = User.query.filter_by(id=int(id)).first()
            return jsonify(
                success=True,
                message="Success",
                data=UserSchema(many=False).dump(user))
        users = User.query.all()
        return jsonify(
            success=True,
            message="Success",
            data=UserSchema(many=True).dump(users))
    if request.method == 'POST':
        data = request.json
        user = User(
            firstname=data.get("firstname", ""),
            lastname=data.get("lastname", ""),
            middlename=data.get("middlename", ""),
            birthday=data.get("birthday", ""),
            address=data.get("address", ""),
        )
        db.session.add(user)
        db.session.commit()
        response = jsonify(
            success=True,
            message='Success',
            data=data
        )
        return response
    if request.method == 'PUT':
        if id:
            data = request.json
            user = User.query.filter_by(id=int(id)).first()
            user.firstname = data.get("firstname")
            user.lastname = data.get("lastname")
            user.middlename = data.get("middlename")
            user.birthday = data.get("birthday")
            user.address = data.get("address")
            db.session.commit()
            return jsonify(
                success=True,
                message='Success'
            )
    if request.method == 'DELETE':
        if id:
            user = User.query.filter_by(id=int(id)).first()
            db.session.delete(user)
            db.session.commit()
            return jsonify(
                success=True,
                message='Success'
            )



