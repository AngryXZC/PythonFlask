from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
# 取环境变量的类
import os
app = Flask(__name__)

app.config.from_pyfile("config/base_setting.py")
# ops_config=local|production
# linux export ops_config=local|production
# windows set ops_config=local|production

if "ops_config" in os.environ:
    app.config.from_pyfile("config/%s_setting.py" % (os.environ['ops_config']))
else:
    app.logger.error("环境变量未配置！")

db = SQLAlchemy(app)


manager = Manager(app)
