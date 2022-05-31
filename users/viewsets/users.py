from flask import Blueprint, request, jsonify

from faker import Faker

import json

users_router = Blueprint('users', __name__, url_prefix='/users')

@users_router.route('/', methods=['GET'])
def users():
    arr = []
    faker = Faker()

    for i in range(10): 
        data =  {
            'firstname': faker.first_name(),
            'lastname': faker.last_name(),
            'middlename' :faker.last_name(),
            'birthday': faker.date(),
            'address': faker.address() 
        }
        arr.append(data)

    return jsonify(data=arr)

