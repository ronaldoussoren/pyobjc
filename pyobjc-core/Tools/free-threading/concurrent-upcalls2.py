from _tools import run_multiple_in_threads
import objc
import time

NSArray = objc.lookUpClass("NSArray")
NSObject = objc.lookUpClass("NSObject")

storage = None


def f(arr, b):
    b.wait()
    arr.makeObjectsPerformSelector_(b"method")
    return


def g(b):
    global storage
    b.wait()
    str(storage)
    del storage
    time.sleep(0.1)
    try:
        str(storage)
        del storage
    except NameError:
        pass


class MyObject(NSObject):
    def method(self):
        global storage
        storage = self
        time.sleep(0.5)
        return 42


with objc.autorelease_pool():
    o = MyObject.alloc().init()
    arr = NSArray.arrayWithArray_([o, o, o, o])
    del o

run_multiple_in_threads((f, (arr,)), (g, ()))
