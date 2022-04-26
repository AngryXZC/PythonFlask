
class Foo(object):
    def __init__(self,func) -> None:
        self._func=func
    def __call__(self, *args, **kwds) :
        print("class decorator runing")
        self._func()
        print("class decorator ending")
@Foo
def bar():
    print("I am bar")




bar()