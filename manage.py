from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis


class Config(object):
    """项目配置信息"""
    DEBUG = True

    # mysql数据库配置信息
    # 数据库连接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1@3306/information19"
    # 关闭数据库修改跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis数据库配置信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_NUM = 9


# 创建app对象
app = Flask(__name__)
# 将配置类注册到app上
app.config.from_objeect(Config)

# 2.创建数据库对象
db = SQLAlchemy(app)

# 3.创建redis数据库对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_NUM)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
