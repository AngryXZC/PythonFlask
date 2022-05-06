'''视图方法'''
from flask import Flask,Blueprint

index_page=Blueprint("index_page",__name__)


@index_page.route("/")
def index_page_page_index():
    return "index page"


@index_page.route("/me")
def hello():
    return "hello "

