from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 实例化flask
app = Flask(__name__)
# 进行数据库的配置
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# 数据库的用户名
username = "root"
# 数据库的密码
pwd = "123456"
# 数据库的ip地址
ip = "10.241.110.1"
# 数据库的端口
port = 3306
# 数据库的库名
database = "testapi"
# 设置mysql 数据库的连接
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# sqlalcchemy绑定app
db = SQLAlchemy(app)


# 每个类表示的是一张表
class test_case(db.Model):
    # 每一个类的变量表示数据库的一个表头
    # db.Column定义表头格式  类型  primary_key是否主键
    id = db.Column(db.Integer, primary_key=True)
    # 字符串  括号里边是最大的长度 unique 是否允许重复，nullable 是否允许为空
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    info = db.Column(db.String(10))

    # 魔法方法 定义打印的格式
    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    # 新建表
    db.create_all()
