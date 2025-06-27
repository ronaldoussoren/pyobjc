from _tools import run_in_threads
import objc

NSObject = objc.lookUpClass("NSObject")

all_dicts = []


class C(NSObject):
    pass


def f(o, b):
    b.wait()

    d = o.__dict__
    assert isinstance(d, dict)
    all_dicts.append(d)


value = C()

run_in_threads(f, (value,))

if not all(x is all_dicts[0] for x in all_dicts):
    print("__dict__ is not the same in all threads")
