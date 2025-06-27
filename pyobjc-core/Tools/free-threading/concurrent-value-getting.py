from _tools import run_in_threads
import objc

NSArray = objc.lookUpClass("NSArray")
NSObject = objc.lookUpClass("NSObject")


def f(a, r, b):
    b.wait()

    v = set()
    for _ in range(100):
        v.add(objc.pyobjc_id(a[0]))
        v.add(objc.pyobjc_id(a[1]))

    r.update(v)


e = set()
with objc.autorelease_pool():
    arr = NSArray.arrayWithArray_([NSObject.alloc().init(), NSObject.alloc().init()])
    e.add(objc.pyobjc_id(arr[0]))
    e.add(objc.pyobjc_id(arr[1]))

r = set()
run_in_threads(f, (arr, r))
assert r == e, f"{r=} != {e=}"
