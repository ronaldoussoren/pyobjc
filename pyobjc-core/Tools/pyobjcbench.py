#!/usr/bin/env python
"""
Script for gathering performance statistics.

This is very much a work in progress, and will morph into a tool
similar to pybench, but just measuring the speed of a number of
PyObjC primitives:

* For methods, functions and blocks:

  - Call with 0, 1, 5 simple arguments
  - Same with by reference arguments

* For methods:
  - Attribute lookup
  - Attribute lookup + call (e.g. how they are usually called)

* objc.repythonify for a number of types

* Add benchmark with ctypes for calling functions

"""

import textwrap
import timeit
import sys
import pathlib

import objc

if len(sys.argv) == 2 and sys.argv[1] == "--record":
    records_dir = pathlib.Path(__file__).parent / "results"
    if not records_dir.is_dir():
        records_dir.mkdir()

    record_fp = open(
        records_dir / f"pyobjcbench-{objc.__version__}.txt",
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
def bound_method_call():
    print_bench(
        "object description bound call",
        timeit.timeit(setup="m = object().__repr__", stmt="m()"),
    )
    print_bench(
        "NSObject description bound call",
        timeit.timeit(
            setup='import objc; NSObject = objc.lookUpClass("NSObject"); '
            "m = NSObject.alloc().init().description",
            stmt="m()",
        ),
    )
    print_bench(
        "NSArray description bound call",
        timeit.timeit(
            setup='import objc; NSArray = objc.lookUpClass("NSArray"); '
            "m = NSArray.alloc().init().description",
            stmt="m()",
        ),
    )
    print()


@benchmark
def unbound_method_call():
    print_bench(
        "object description unbound call",
        timeit.timeit(setup="o = object()", stmt="o.__repr__()"),
    )
    print_bench(
        "NSObject description unbound call",
        timeit.timeit(
            setup='import objc; NSObject = objc.lookUpClass("NSObject"); '
            "o = NSObject.alloc().init()",
            stmt="o.description()",
        ),
    )
    print_bench(
        "NSArray description unbound call",
        timeit.timeit(
            setup='import objc; NSArray = objc.lookUpClass("NSArray"); '
            "o = NSArray.alloc().init()",
            stmt="o.description()",
        ),
    )
    print()


@benchmark
def imp_call():
    print_bench(
        "object description IMP call",
        timeit.timeit(setup="o = object(); m = object.__repr__", stmt="m(o)"),
    )
    print_bench(
        "NSObject description IMP call",
        timeit.timeit(
            setup='import objc; NSObject = objc.lookUpClass("NSObject"); '
            "o = NSObject.alloc().init(); m = o.methodForSelector_(b'description')",
            stmt="m(o)",
        ),
    )
    print_bench(
        "NSArray description IMP call",
        timeit.timeit(
            setup='import objc; NSArray = objc.lookUpClass("NSArray"); '
            "o = NSArray.alloc().init(); m = o.methodForSelector_(b'description')",
            stmt="m(o)",
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
    # XXX: This needs a helper module, there's unnecessary
    #      overhead in statement under test.
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


# @benchmark
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
