# FlaskMovie Demo 说明文档
1. 记录Python的一些语法规则（常见的）
2. 记录Flask研究的笔记
3. 记录对于网站开发的一些思考和疑问
## Python篇
1. python 中加入 ___name__="main"到底有什么作用？
    + <font color=red>  在其他文件引入该文件时确定当前文件执行代码段与引入文件的代码段不冲突。</font>
    + 已解决（就是确定入口文件的）
## Flask篇
1. WIndows 设置环境变量使用set ops_config=local不好使，使用$env:ops_config="local"好使（使用CMD不好使，使用Shell好使）
2.  有时间可以研究一下Flask底层的Werkzeug(Flask底层的框架)
3. Flask 根据表结构自动生成model:
    + flask-sqlacodegen插件
        + pip install flask-sqlacodegen
        + flask-sqlacodegen 'mysql://root:123456@127.0.0.1/mysql' --tables user --outfile "common/models/user.py" --flask
    + 通过model生成表结构
        + from common.models.user import user
        + db.Model=User
        + db.creat_all()
## Flask MVC篇
### MVC构建篇
1. 将c层放在controllers文件夹下
2. application.py 负责初始化一些参数：app,db
3. manager 负责启动
4. www负责路由注册
5. 将template下的文件改为继承自模板页面
### MVC 优化篇
+ flask_scripts 自定义启动命令(管理启动命令)
+ 多环境配置文件
+ flask_debugtoolbar
+ 错误处理器
+ 请求拦截器
# 可能遇到的问题以及解决方法：
1. ModuleNotFoundError: No module named 'flask._compat'：Flask版本太高指定Flask版本为1.1.4
2. ImportError: cannot import name 'soft_unicode' from 'markupsafe'：markupsafe版本指定为 2.0.1
+ 进行到环境变量配置