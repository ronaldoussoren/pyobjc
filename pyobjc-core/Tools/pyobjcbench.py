#!/usr/bin/env python
"""
Script for gathering performance statistics.

This is very much a work in progress, and will morph into a tool
simular to pybench, but just measuring the speed of a number of
PyObjC primitives:

* For methods, functions and blocks:

  - Call with 0, 1, 5 simple arguments
  - Same with by reference arguments

* For methods:
  - Attribute lookup
  - Attribute lookup + call (e.g. how they are usually called)

* objc.repythonify for a number of types

"""
from __future__ import print_function

import timeit

import objc


def print_bench(title, time):
    print(f"{title:30s}: {time:.3f}")


NSObject = objc.lookUpClass("NSObject")
NSArray = objc.lookUpClass("NSArray")

print_bench(
    "object description lookup", timeit.timeit(setup="o = object()", stmt="o.__repr__")
)
print_bench(
    "NSObject description lookup",
    timeit.timeit(
        setup='import objc; NSObject = objc.lookUpClass("NSObject"); '
        "o = NSObject.alloc().init()",
        stmt="o.description",
    ),
)
print_bench(
    "NSArray description lookup",
    timeit.timeit(
        setup='import objc; NSArray = objc.lookUpClass("NSArray"); '
        "o = NSArray.alloc().init()",
        stmt="o.description",
    ),
)
print()
print_bench(
    "object description call",
    timeit.timeit(setup="m = object().__repr__", stmt="m()"),
)
print_bench(
    "NSObject description call",
    timeit.timeit(
        setup='import objc; NSObject = objc.lookUpClass("NSObject"); '
        "m = NSObject.alloc().init().description",
        stmt="m()",
    ),
)
print_bench(
    "NSArray description call",
    timeit.timeit(
        setup='import objc; NSArray = objc.lookUpClass("NSArray"); '
        "m = NSArray.alloc().init().description",
        stmt="m()",
    ),
)
print()
print_bench(
    "python function call",
    timeit.timeit(setup="import math; f=math.sin", stmt="f(5.0)"),
)
setup = """
import objc
objc.loadBundleFunctions(None, globals(), [("sin", b"dd")])
f = sin
"""
print_bench(
    "objc function call",
    timeit.timeit(setup=setup, stmt="f(5.0)"),
)
