'''路由注册'''
from interceptor.auth import*
from interceptor.error_handler import*
from application import app

from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)
'''
拦截器处理和错误处理器
'''
from interceptor.error_handler import*
from interceptor.auth import*


'''蓝图'''
from controllers.index import index_page
from controllers.member import member_page
app.register_blueprint(index_page, url_prefix="/")
app.register_blueprint(member_page,url_prefix="/member")

'''
模板函数
'''
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl,"buildStaticUrl")
app.add_template_global(UrlManager.buildUrl,'buildUrl')