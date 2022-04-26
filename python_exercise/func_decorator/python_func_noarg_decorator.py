'''装饰器'''
'''函数装饰器'''
#原始
# def bar():
#     print("[Debug] bar is running")
#     print("i am bar!")
# def bar2():
#     print("[Debug] bar2 is running")
#     print("i am bar2!")
# bar();
# bar2();
#装饰器


#传统调用
# def use_logging(func_name):
#     #print("[debug]"+func_name+"is running")
#     print("[debug]%sis running"% func_name)
#装饰器引用
def use_logging(func):
        #print("[debug]"+func_name+"is running")
    def wrapper(*args,**kwrags):
        print("[debug]%s is running"% func.__name__)
        return func(*args, **kwrags)
    return wrapper
#注解应用
@use_logging
def bar():
    # use_logging("bar")
    print("i am bar!")
@ use_logging
def bar2():
    # use_logging("bar2")
    print("i am bar2!")
# bar();
# bar2();
#使用古老的方式装饰器
# bar=use_logging(bar)
# bar2 =use_logging(bar2)
# bar()
# bar2()
bar()
bar2()