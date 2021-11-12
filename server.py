from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
# 解决跨域问题
CORS(app, supports_credentials=True)
username = "root"
pwd = "123456"
ip = "10.241.110.1"
port = 3306
database = "testapi"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


def router():

    from api import TestCaseServer
    api.add_resource(TestCaseServer, '/testcase')

if __name__ == '__main__':
    router()
    app.run(debug=True)
