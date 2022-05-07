'''视图方法'''
from unicodedata import name
from urllib import response
from flask import Flask,Blueprint, request,make_response,jsonify,render_template
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

'''
返回不同的值
'''
#字符串
@index_page.route("/text")
def text():
    return "text/html"


@index_page.route("/text_same")
def text_same():
    response=make_response("text/html",200)
    return response
#Json
@index_page.route("/json")
def json():
    import json
    data={"a":"b"}
    response=make_response(json.dumps(data))
    response.headers["Content-Type"]="application/json"
    return response
@index_page.route("/json_same")
def json_same():
    data={"a":"b"}
    response=make_response(jsonify(data))
    return response
#template
@index_page.route("/template")
def template():
    ##传值
   name="xzc"
  #  return render_template("index.html",name=name)
   context={"name":name}
   context['user']={"nickName":"AngryLeesin","qq":"1079916791","home_page":"https://github.com/AngryXZC/PythonFlask"}
   context['num_list']=[1,2,3,4,5]
   return render_template("index.html",**context)

@index_page.route("/extend_template")
def extend_template():
    return render_template("extend_template.html")