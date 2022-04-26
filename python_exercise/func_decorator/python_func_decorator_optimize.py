'''装饰器'''
'''函数装饰器(带参数)'''
import functools
#装饰器引用(加上函数装饰器应用后不丢失函数信息)
def use_logging(level="Debug"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwrags):
            print("[%s]%s is running" % (level,func.__name__))
            return func(*args, **kwrags)
        return wrapper
    return decorator
#注解应用
# @use_logging(level="info")
def bar():
    print("i am bar!")
f=use_logging(level="warn")(bar)
f()
print(f.__name__)
print(f.__doc__)