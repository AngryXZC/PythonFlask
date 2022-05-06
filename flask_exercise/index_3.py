'''路由注册蓝图优化'''
from flask import Flask,Blueprint
app=Flask(__name__)

index_page=Blueprint("index_page",__name__)
@index_page.route("/")
def index_page_page_index():
    return "index page"

app.register_blueprint(index_page,url_prefix="/xzc")

@app.route("/")
def hello():
    return "Hellw Flask!"

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)