'''视图注册'''
import imp
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from indexController import index_page
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@127.0.0.1/mysql"
db=SQLAlchemy(app)
app.register_blueprint(index_page,url_prefix="/xzc")
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)