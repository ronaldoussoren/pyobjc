from _tools import run_multiple_in_threads
import objc

NSArray = objc.lookUpClass("NSArray")
NSMutableArray = objc.lookUpClass("NSMutableArray")


def clearer(b):
    global gArray1
    b.wait()
    gArray1 = None


def setter(b):
    b.wait()
    gArray2.addObject_(gValue)


for _ in range(50):
    gValue = object()
    gArray1 = NSArray.alloc().initWithArray_([gValue])
    gArray2 = NSMutableArray.alloc().initWithArray_([gValue])
    run_multiple_in_threads(
        (clearer, ()), (clearer, ()), (setter, ()), (setter, ()), (setter, ())
    )
