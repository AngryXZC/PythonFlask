'''装饰器'''
'''函数装饰器(带参数)'''
#装饰器引用
def use_logging(level="Debug"):
    def decorator(func):
        def wrapper(*args, **kwrags):
            print("[%s]%s is running" % (level,func.__name__))
            return func(*args, **kwrags)
        return wrapper
    return decorator
#注解应用
@use_logging(level="info")
def bar():
    print("i am bar!")
@ use_logging(level="warn")
def bar2():
    print("i am bar2!")
bar()
bar2()
'''函数装饰器优缺点分析'''
#使用装饰器极大的复用了代码，但是他有一个缺点就是原函数的元信息不见了
#比如函数的docstring、_name_、参数列表