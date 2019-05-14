from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


class Config(object):
    """项目的配置"""
    DEBUG = True

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db_rento"  # mysql://username:password@ip:port/dbname
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 集成flask-script
manager = Manager(app)
# 将 app 与 db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    manager.run()
