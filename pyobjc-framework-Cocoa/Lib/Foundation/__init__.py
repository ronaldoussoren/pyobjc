"""
Python mapping for the Foundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import CoreFoundation
import Foundation._Foundation
import objc
from Foundation import _metadata
from Foundation._inlines import _inline_list_

objc.addConvenienceForClass(
    "NSAttributedString", (("__len__", lambda self: self.length()),)
)

objc.addConvenienceForBasicMapping("NSMergeConflict", True)
objc.addConvenienceForBasicMapping("NSUbiquitousKeyValueStore", False)
objc.addConvenienceForBasicMapping("NSUserDefaults", False)


def _setup_conveniences():
    NSNull = objc.lookUpClass("NSNull")

    def nscache_getitem(self, key):
        value = self.objectForKey_(key)
        if value is None:
            raise KeyError(key)

        elif value is NSNull.null():
            return None

        else:
            return value

    def nscache_get(self, key, default=None):
        value = self.objectForKey_(key)
        if value is None:
            return default
        elif value is NSNull.null():
            return None
        return value

    def nscache_setitem(self, key, value):
        if value is None:
            value = NSNull.null()
        self.setObject_forKey_(value, key)

    objc.addConvenienceForClass(
        "NSCache",
        (
            ("__getitem__", nscache_getitem),
            ("get", nscache_get),
            ("__setitem__", nscache_setitem),
            ("__delitem__", lambda self, key: self.removeObjectForKey_(key)),
            ("clear", lambda self: self.removeAllObjects()),
        ),
    )

    def hash_add(self, value):
        if value is None:
            value = NSNull.null()
        self.addObject_(value)

    def hash_contains(self, value):
        if value is None:
            value = NSNull.null()
        return self.containsObject_(value)

    def hash_remove(self, value):
        if value is None:
            value = NSNull.null()
        self.removeObject_(value)

    def hash_pop(self):
        value = self.anyObject()
        self.removeObject_(value)
        if value is NSNull.null():
            return None
        else:
            return value

    objc.addConvenienceForClass(
        "NSHashTable",
        (
            ("__len__", lambda self: self.count()),
            ("clear", lambda self: self.removeAllObjects()),
            ("__iter__", lambda self: iter(self.objectEnumerator())),
            ("add", hash_add),
            ("remove", hash_remove),
            ("__contains__", hash_contains),
            ("pop", hash_pop),
        ),
    )

    objc.addConvenienceForClass(
        "NSIndexPath", (("__len__", lambda self: self.count()),)
    )

    if sys.maxsize > 2**32:
        NSNotFound = 0x7FFFFFFFFFFFFFFF
    else:
        NSNotFound = 0x7FFFFFFF

    def indexset_iter(self):
        value = self.firstIndex()
        while value != NSNotFound:
            yield value
            value = self.indexGreaterThanIndex_(value)

    def indexset_reversed(self):
        value = self.lastIndex()
        while value != NSNotFound:
            yield value
            value = self.indexLessThanIndex_(value)

    NSIndexSet = objc.lookUpClass("NSIndexSet")

    def indexset_eq(self, other):
        if not isinstance(other, NSIndexSet):
            return False

        return self.isEqualToIndexSet_(other)

    def indexset_ne(self, other):
        if not isinstance(other, NSIndexSet):
            return True

        return not self.isEqualToIndexSet_(other)

    def indexset_contains(self, value):
        try:
            return self.containsIndex_(value)
        except ValueError:
            return False

    objc.addConvenienceForClass(
        "NSIndexSet",
        (
            ("__len__", lambda self: self.count()),
            ("__iter__", indexset_iter),
            ("__reversed__", indexset_reversed),
            ("__eq__", indexset_eq),
            ("__ne__", indexset_ne),
            ("__contains__", indexset_contains),
        ),
    )

    # Add 'update', '-=', '+='
    objc.addConvenienceForClass(
        "NSMutableIndexSet",
        (
            ("clear", lambda self: self.removeAllIndexes()),
            ("add", lambda self, value: self.addIndex_(value)),
            ("remove", lambda self, value: self.removeIndex_(value)),
        ),
    )

    objc.addConvenienceForClass(
        "NSLocale", (("__getitem__", lambda self, key: self.objectForKey_(key)),)
    )


_setup_conveniences()

sys.modules["Foundation"] = mod = objc.ObjCLazyModule(
    "Foundation",
    "com.apple.Foundation",
    objc.pathForFramework("/System/Library/Frameworks/Foundation.framework"),
    _metadata.__dict__,
    _inline_list_,
    {
        "__doc__": __doc__,
        "objc": objc,
        "YES": objc.YES,
        "NO": objc.NO,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (CoreFoundation,),
)


del sys.modules["Foundation._metadata"]


for nm in dir(Foundation._Foundation):
    if nm.startswith("_"):
        continue
    setattr(mod, nm, getattr(Foundation._Foundation, nm))


mod.NSDecimal = objc.NSDecimal

import Foundation._context  # isort:skip  # noqa: E402
import Foundation._functiondefines  # isort:skip  # noqa: E402
import Foundation._nsindexset  # isort:skip  # noqa: E402
import Foundation._nsobject  # isort:skip  # noqa: E402

for nm in dir(Foundation._functiondefines):
    setattr(mod, nm, getattr(Foundation._functiondefines, nm))


mod.NSIntegerMax = sys.maxsize
mod.NSIntegerMin = -sys.maxsize - 1
mod.NSUIntegerMax = (sys.maxsize * 2) + 1


for nm in dir(Foundation._context):
    setattr(mod, nm, getattr(Foundation._context, nm))
