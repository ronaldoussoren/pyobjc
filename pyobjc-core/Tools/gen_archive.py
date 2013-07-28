#!/usr/bin/env python
import sys
import objc

from Foundation import NSArchiver, NSKeyedArchiver

class Class1:
    pass

class Class2 (object):
    pass


def gen_archive(fname, archiver):
    o1 = Class1()
    o2 = Class2()

    o1.a = 42
    o1.b = 2.5

    o2.obj = o1
    o2.lst = [1,2,3]
    o2.string = "hello world"

    archiver.archiveRootObject_toFile_(o2, fname)


def main():
    fname = 'py%s-oc%s.%s'%(
            sys.version_info[:1] +
            tuple(objc.__version__.replace('a', '.').replace('b', '.').split('.')[:2]))

    gen_archive(fname + '.plain', NSArchiver)
    gen_archive(fname + '.keyed', NSKeyedArchiver)

if __name__ == "__main__":
    main()
