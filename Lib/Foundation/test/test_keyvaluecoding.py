import unittest
import objc

from Foundation import *
from PyObjCTools import KeyValueCodingSupport

class StraightPython(KeyValueCodingSupport.KeyValueCoding):
    foo = 21
    bar = 42
    baz = { "bob" : "tail" }
    _didBar = 0
    def bar(self):
        self._didBar = 1
        return self._bar
    def setBar(self, aValue):
        self._bar = aValue
    def didBar(self): return self._didBar

class PyObjCMix(NSObject):
    foo = 21
    bar = 42
    baz = { "bob" : "tail" }
    _didBar = 0
    def bar(self):
        self._didBar = 1
        return self._bar
    def setBar(self, aValue):
        self._bar = aValue
    def didBar(self): return self._didBar

class TestKeyValueCoding(unittest.TestCase):
    def testValueForKey(self):
        KeyValueCodingSupport.addKeyValueBridgeToClass(PyObjCMix)

        a = StraightPython()
        b = PyObjCMix.new()

        self.assertEqual(a.valueForKey_("foo"), 21)
        self.assertEqual(b.valueForKey_("foo"), 21)
        self.assertEqual(a.didBar(), 0)
        self.assertEqual(b.didBar(), 0)
        self.assertEqual(a.valueForKey_("bar"), 42)
        self.assertEqual(b.valueForKey_("bar"), 42)
        self.assertEqual(a.didBar(), 1)
        self.assertEqual(b.didBar(), 1)

if __name__ == '__main__':
    unittest.main( )
