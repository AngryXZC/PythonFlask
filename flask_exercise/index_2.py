
'''路由注册'''
from pickle import TRUE
from re import M
from flask import Flask
app=Flask(__name__)
'''通过函数装饰器定义路由'''
#@app.route("/")
def hello():
    return "Hello Flask!"
'''参数'''
#@app.route("/my/<user_name>")
def my(user_name):
    return "my page:user: %s"%(user_name)

'''通过add_url_rule定义路由规则'''

app.add_url_rule(rule="/",view_func=hello)
app.add_url_rule(rule="/my/<user_name>",view_func=my)


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)