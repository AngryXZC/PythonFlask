from pickle import TRUE
from flask import Flask
app=Flask(__name__)
'''以变量的方式加载'''
#app.config["DEBUG"]=TRUE
'''以模块的方式加载'''
#app.config.from_object("config")
'''以环境变量的方式加载'''
app.config.from_envvar("ops_config")
'''以文件配置进行加载'''
#app.config.from_pyfile("config.py")
@app.route("/")
def hello():
    return "Hello Flask!"
if __name__=="__main__":
    app.run(host="0.0.0.0")