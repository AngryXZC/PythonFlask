# 本地开发环境配置
from config.base_setting import*

# SQLALCHEMY_ECHO = False
# SQLALCHEMY_TRACK_MODIFICATIONS = True

# 虚拟机数据库连接
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/mysql"
# 本地数据库连接
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1/mysql"
SECRET_KEY = "xzcLocal"
