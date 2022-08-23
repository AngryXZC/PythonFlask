'''路由注册'''
from interceptor.auth import*
from interceptor.error_handler import*
from application import app
from controllers.index import index_page
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)
'''
拦截器处理和错误处理器
'''
app.register_blueprint(index_page, url_prefix="/")
