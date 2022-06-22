'''视图方法'''
from flask import Blueprint,render_template
#代码分层解决的问题
from common.models.user import User
index_page=Blueprint("index_page",__name__)
@index_page.route("/")
def index():
    ##传值
   name="xzc"
  #  return render_template("index.html",name=name)
   context={"name":name}
   context['user']={"nickName":"AngryLeesin","qq":"1079916791","home_page":"https://github.com/AngryXZC/PythonFlask"}
   context['num_list']=[1,2,3,4,5]
   
   ###查询数据库
   
#    sql = text("SELECT * FROM `user`")
   
#    result=db.engine.execute(sql)
#通过实体访问数据库
   result=User.query.all()
   context['result']=result
   return render_template("index.html",**context)
