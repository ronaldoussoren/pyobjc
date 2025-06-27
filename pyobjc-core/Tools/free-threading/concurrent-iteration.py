from _tools import run_in_threads
import objc

NSArray = objc.lookUpClass("NSArray")

A_LEN = 100


def f(a, e, b):
    b.wait()

    s = 0
    for i in a:
        s += i

    if s != e:
        print(f"Expected sum {e}, got {s}")


arr = NSArray.arrayWithArray_(list(range(A_LEN)))
expected = sum(range(A_LEN))

run_in_threads(f, (arr, expected))
