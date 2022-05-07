'''视图方法'''
from flask import Flask,Blueprint, request

index_page=Blueprint("index_page",__name__)


@index_page.route("/")
def index_page_page_index():
    return "index page"


@index_page.route("/me")
def hello():
    return "hello "

@index_page.route("/get")
def get():
    req=request.values
    #变种
    var_a=req['a'] if "a" in req else "i love flask"
   # var_a=  request.args.get("a","i love flask")
    return "request:%s,params:%s,var_a:%s"%(request.method,request.args,var_a)






@index_page.route("/post",methods = ["POST"])
def post():
    #var_a=  request.form['a'] if "a" in request.form else ''
    req=request.values
    #变种
    var_a=req['a'] if "a" in req else "i love flask"
    return "request:%s,params:%s,var_a:%s"%(request.method,request.form,var_a)

@index_page.route("/upload",methods=["POST"])
def upload():
    f=request.files['file'] if "file" in request.files else ''
    return "request:%s,params:%s,file:%s"%(request.method,request.files,f)
        