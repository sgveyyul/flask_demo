from flask import Flask

from users.viewsets.users import users_router

app = Flask(__name__)

app.register_blueprint(users_router)

if __name__=='__main__':
    app.run(host='localhost', port=8080, debug=True)