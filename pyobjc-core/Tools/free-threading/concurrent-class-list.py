from _tools import run_in_threads
import objc


def f(b):
    b.wait()
    objc.getClassList()
    return


run_in_threads(f, ())
