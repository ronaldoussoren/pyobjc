#!/usr/bin/env python
"""
Experimental code, attempting to work around Apple's KVO hacks.
"""

import objc
from Foundation import (
    NSObject,
    NSKeyValueObservingOptionOld,
    NSKeyValueObservingOptionNew,
)


_kvoclassed = {}


def dumpClass(cls):
    print("DUMP", cls)
    print(cls.__bases__)
    # for k, v in cls.__dict__.items():
    #    print k, v
    print("-" * 40)


def toKVOClass(orig, new):
    if new in _kvoclassed:
        return new
    origdct = dict(orig.__dict__)
    origset = set(origdct)
    newset = set(new.__dict__)
    # Merge in non-methods from the dict
    for key in origset - newset:
        value = origdct[key]
        if isinstance(value, objc.selector):
            continue
        setattr(new, key, value)
    # Remember the original class,
    # KVO wants to go back to NSObject!
    _kvoclassed[new] = orig
    return new


def fromKVOClass(new):
    return _kvoclassed[new]


class FooClass(NSObject):
    _kvc_bar = None
    outlet = objc.IBOutlet("outlet")

    def XXaddObserver_forKeyPath_options_context_(
        self, observer, keyPath, options, context
    ):
        print(
            "addObserver_forKeyPath_options_context_",
            observer,
            keyPath,
            options,
            context,
        )
        orig = FooClass  # type(self)
        super(orig, self).addObserver_forKeyPath_options_context_(
            observer, keyPath, options, context
        )
        new = self.class__()
        print(orig, type(self), new)
        if orig is not new:
            print("class changed!!")
            self.__class__ = toKVOClass(orig, new)

    def XXremoveObserver_forKeyPath_(self, observer, keyPath):
        print("removeObserver_forKeyPath_", observer, keyPath)
        orig = type(self)
        super(orig, self).removeObserver_forKeyPath_(observer, keyPath)
        new = self.class__()
        print(orig, type(self), new)
        if orig is not new:
            print("class changed!!")
            self.__class__ = fromKVOClass(orig)

    def setBar_(self, bar):
        print("setBar_ ->", bar)
        print(self, type(self), self.class__())
        # print('->', bar)
        self._kvc_bar = bar

    setBar_ = objc.accessor(setBar_)

    def bar(self):
        print("bar", self._kvc_bar)
        # print(self, type(self), self.class__())
        return self._kvc_bar

    bar = objc.accessor(bar)


class FooObserver(NSObject):
    def observeValueForKeyPath_ofObject_change_context_(
        self, keyPath, obj, change, context
    ):
        print(
            "[[[[[]]]]] observeValueForKeyPath_ofObject_change_context_",
            keyPath,
            obj,
            change,
            context,
        )
        dumpClass(type(obj))

    def willChangeValueForKey_(self, key):
        print("[[[[[]]]]] willChangeValueForKey_", key)


foo = FooClass.alloc().init()
fooObserver = FooObserver.alloc().init()

print()
print()
print("***** unobserved set")
print(foo.bar())
foo.setBar_("0shw00t")
print(foo.bar())

print()
print()
print("***** observing, setting three times")
print("foo's ISA:", foo.pyobjc_ISA)
print("Adding an observer")
foo.addObserver_forKeyPath_options_context_(
    fooObserver, "bar", (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld), 0
)
print("foo's ISA:", foo.pyobjc_ISA)
# foo.removeObserver_forKeyPath_(fooObserver, u'bar');sys.exit(1)
print(foo.bar())
foo.setBar_("1w00t")
print(foo.bar())
foo.setBar_("2sw00t")
print(foo.bar())
foo.setBar_("3shw00t")
print(foo.bar())

print()
print()
print("***** removing the observer and setting twice (unobserved)")
foo.removeObserver_forKeyPath_(fooObserver, "bar")
print(foo.bar())
foo.setBar_("4sw00t")
print(foo.bar())
foo.setBar_("5w00t")
print(foo.bar())

print(foo.__class__)
