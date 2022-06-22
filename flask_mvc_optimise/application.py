from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
#取环境变量的类
import os
app=Flask(__name__)


manager=Manager(app)

app.config.from_pyfile("config/base_setting.py")
#ops_config=local|production
#linux export ops_config=local|production
#windows set ops_config=local|production

#print("环境变量",os.environ)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@127.0.0.1/mysql"
db=SQLAlchemy(app)

