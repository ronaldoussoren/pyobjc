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

import textwrap
import timeit
import sys
import pathlib

import objc

if len(sys.argv) == 2 and sys.argv[1] == "--record":
    record_fp = open(
        pathlib.Path(__file__).parent
        / "results"
        / f"pyobjcbench-{objc.__version__}.txt",
        "w",
    )

    def print_bench(title, time):
        print(f"{title:30s}: {time:.3f}")
        print(f"{title:30s}: {time:.3f}", file=record_fp)

    def print_header(key, value):
        print(f"@{key} {value}")
        print(f"@{key} {value}", file=record_fp)


else:

    def print_bench(title, time):
        print(f"{title:30s}: {time:.3f}")

    def print_header(key, value):
        print(f"@{key} {value}")


NSObject = objc.lookUpClass("NSObject")
NSArray = objc.lookUpClass("NSArray")

BENCHMARKS = []


def benchmark(func):
    BENCHMARKS.append(func)
    return func


@benchmark
def descriptor_lookup():
    print_bench(
        "object description lookup",
        timeit.timeit(setup="o = object()", stmt="o.__repr__"),
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


@benchmark
def descriptor_call():
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


@benchmark
def function_call():
    print_bench(
        "python function call",
        timeit.timeit(setup="import math; f=math.sin", stmt="f(5.0)"),
    )
    setup = textwrap.dedent(
        """\
    import objc
    objc.loadBundleFunctions(None, globals(), [("sin", b"dd")])
    f = sin
    """
    )
    print_bench(
        "objc function call",
        timeit.timeit(setup=setup, stmt="f(5.0)"),
    )


@benchmark
def call_from_objc():
    setup = textwrap.dedent(
        """\
    import objc
    NSObject = objc.lookUpClass("NSObject")
    NSArray = objc.lookUpClass("NSArray")
    class CallFromObjC1(NSObject):
        __slots__ = ("count",)

        def init(self):
            self = super().init()
            self.count = 0
            return self

        def aSelector(self):
            self.count += 1

    o = CallFromObjC1.new()
    a = NSArray.arrayWithArray_([o]*10)
    """
    )

    print_bench(
        "call no-args from objc",
        timeit.timeit(setup=setup, stmt="a.makeObjectsPerformSelector_(b'aSelector')"),
    )


@benchmark
def hasattr_speed():
    print()
    print_bench(
        "hasattr object is True",
        timeit.timeit(setup="o = object()", stmt="hasattr(o, '__repr__')"),
    )
    print_bench(
        "hasattr NSObject is True",
        timeit.timeit(
            setup='import objc; NSObject = objc.lookUpClass("NSObject"); '
            "o = NSObject.alloc().init()",
            stmt="hasattr(o, 'description')",
        ),
    )
    print_bench(
        "hasattr NSArray is True",
        timeit.timeit(
            setup='import objc; NSArray = objc.lookUpClass("NSArray"); '
            "o = NSArray.alloc().init()",
            stmt="hasattr(o, 'description')",
        ),
    )
    print()
    print_bench(
        "hasattr object is False",
        timeit.timeit(setup="o = object()", stmt="hasattr(o, 'attribute')"),
    )
    print_bench(
        "hasattr NSObject is False",
        timeit.timeit(
            setup='import objc; NSObject = objc.lookUpClass("NSObject"); '
            "o = NSObject.alloc().init()",
            stmt="hasattr(o, 'invalidselector')",
        ),
    )
    print_bench(
        "hasattr NSArray is False",
        timeit.timeit(
            setup='import objc; NSArray = objc.lookUpClass("NSArray"); '
            "o = NSArray.alloc().init()",
            stmt="hasattr(o, 'invalidselector')",
        ),
    )
    print()


print_header("python", ".".join(str(x) for x in sys.version_info[:3]))
print_header("objc", objc.__version__)
print()
for func in BENCHMARKS:
    func()
