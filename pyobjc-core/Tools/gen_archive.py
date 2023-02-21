#!/usr/bin/env python
import os
import sys

import objc
from Foundation import NSArchiver, NSKeyedArchiver, NSString

#
# Any updates to class definitions here should also be done
# in PyObjCTest/test_archiving_interop.py
#


class Class1:
    pass


class Class2:
    pass


class Class3:
    def __init__(self):
        self.a = None
        self.b = None

    def __getstate__(self):
        return (self.a, self.b)

    def __setstate__(self, state):
        self.a, self.b = state


class Class4:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def __getstate__(self):
        return {"a": self.a, "b": self.b, NSString.stringWithString_("c"): self.c}


#
# END
#


def gen_archive(fname, archiver):
    # NOTE: Changes to this code should also be done
    #       to the verification code in PyObjCTest/test_archiving_interop.py

    o1 = Class1()
    o2 = Class2()

    o1.a = 42
    o1.b = 2.5

    o2.obj = o1
    o2.lst = [1, 2, 3]
    o2.string = "hello world"
    o2.o3 = Class3()
    o2.o3.a = 42
    o2.o3.b = 21

    o2.o4 = Class4()
    o2.o4.a = "A"
    o2.o4.b = "B"
    o2.o4.c = "C"

    archiver.archiveRootObject_toFile_(o2, fname)


def main():
    fname = "py%s-oc%s.%s" % (
        sys.version_info[:1]
        + tuple(objc.__version__.replace("a", ".").replace("b", ".").split(".")[:2])
    )
    fname = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "PyObjCTest",
        "archives",
        fname,
    )

    gen_archive(fname + ".plain", NSArchiver)
    gen_archive(fname + ".keyed", NSKeyedArchiver)


if __name__ == "__main__":
    main()
