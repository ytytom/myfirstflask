from flask import Flask
from flask_restful import Api
from .admin import admin
# from flask import render_template

app = Flask(__name__)
app.register_blueprint(admin)
api = Api(app)


@app.route('/index/')
def index():
    return 'this is index'


