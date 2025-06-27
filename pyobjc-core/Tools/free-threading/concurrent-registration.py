from _tools import run_in_threads
import objc

NSArray = objc.lookUpClass("NSArray")

all_dicts = []


value = [1, 2, 3]

NSArray.alloc().initWithArray_(value)


def f(o, b):
    b.wait()

    with objc.autorelease_pool():
        a = NSArray.arrayWithArray_(value)
        del a


run_in_threads(f, (value,))
