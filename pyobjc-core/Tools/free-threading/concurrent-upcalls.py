from _tools import run_in_threads
import objc

NSArray = objc.lookUpClass("NSArray")
NSObject = objc.lookUpClass("NSObject")


def f(arr, b):
    b.wait()
    arr.makeObjectsPerformSelector_(b"method")
    return


class MyObject(NSObject):
    def method(self):
        return 42


with objc.autorelease_pool():
    o = MyObject.alloc().init()
    arr = NSArray.arrayWithArray_([o, o, o, o])
    del o

run_in_threads(f, (arr,))
