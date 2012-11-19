# Tests for PyObjCTools.KeyValueCoding
from PyObjCTools.TestSupport import *

from PyObjCTools import KeyValueCoding
import operator


class TestHelpers (TestCase):
    def test_msum(self):
        self.assertEqual(KeyValueCoding.msum([1, 1e100, 1, -1e100] * 10000), 20000)
        self.assertEqual(KeyValueCoding.msum([1.0, 2.0, 3.0, 4.0]), 10.0)

    def test_keyCaps(self):
        self.assertEqual(KeyValueCoding.keyCaps("attr"), "Attr")
        self.assertEqual(KeyValueCoding.keyCaps("Attr"), "Attr")
        self.assertEqual(KeyValueCoding.keyCaps("AttR"), "AttR")
        self.assertEqual(KeyValueCoding.keyCaps("attr_with_value"), "Attr_with_value")

        self.assertEqual(KeyValueCoding.keyCaps(b"attr"), b"Attr")
        self.assertEqual(KeyValueCoding.keyCaps(b"Attr"), b"Attr")
        self.assertEqual(KeyValueCoding.keyCaps(b"AttR"), b"AttR")
        self.assertEqual(KeyValueCoding.keyCaps(b"attr_with_value"), b"Attr_with_value")


class TestArrayOperators (TestCase):
    def test_missing(self):
        self.fail("Missing tests for ArrayOperators")

class TestPythonObject (TestCase):
    def test_missing(self):
        self.fail("Missing tests for KVC on Python objects")


class TestObjectiveCObject (TestCase):
    def test_missing(self):
        self.fail("Missing tests for KVC on Cocoa objects")


class TestMixed (TestCase):
    def test_missing(self):
        self.fail("Test keypath operations on mixed graphs")


class TestKVCHelper (TestCase):
    def setUp(self):
        self._orig = {
            'getKey': KeyValueCoding.getKey,
            'setKey': KeyValueCoding.setKey,
            'getKeyPath': KeyValueCoding.getKeyPath,
            'setKeyPath': KeyValueCoding.setKeyPath,
        }
        self._trace = []
        def getKey(obj, k):
            self._trace.append(('get', obj, k))
        def setKey(obj, k, v):
            self._trace.append(('set', obj, k, v))
        def getKeyPath(obj, k):
            self._trace.append(('get-path', obj, k))
        def setKeyPath(obj, k, v):
            self._trace.append(('set-path', obj, k, v))
        KeyValueCoding.getKey = getKey
        KeyValueCoding.setKey = setKey
        KeyValueCoding.getKeyPath = getKeyPath
        KeyValueCoding.setKeyPath = setKeyPath


    def tearDown(self):
        for k in self._orig:
            setattr(KeyValueCoding, k, self._orig[k])

    def test_repr(self):
        for o in [
                object(), 42, "42", b"42", b"42".decode('latin1')
                ]:
            self.assertEqual(repr(KeyValueCoding.kvc(o)), repr(o))

    def test_attribute_access(self):
        v = object()
        o = KeyValueCoding.kvc(v)
        o.key
        o.key2
        getattr(o, "key3.key4")
        self.assertEqual(self._trace,  [
            ('get', v, 'key'),
            ('get', v, 'key2'),
            ('get', v, 'key3.key4'),
        ])
        self._trace[:] = []

        o.key = 42
        setattr(o, "key3.key4", 99)
        self.assertEqual(self._trace,  [
            ('set', v, 'key', 42),
            ('set', v, 'key3.key4', 99),
        ])
        self._trace[:] = []

        class Object (object):
            pass

        v = Object()
        o = KeyValueCoding.kvc(v)
        o.key = 42
        o._key = 99
        self.assertEqual(self._trace,  [
            ('set', v, 'key', 42),
        ])
        self.assertEqual(o._key, 99)
        self.assertIn('_key', o.__dict__)
        self.assertNotIn('key', o.__dict__)


    def test_item_access(self):
        v = object()
        o = KeyValueCoding.kvc(v)
        o['key']
        o['key2']
        o['key3.key4']
        self.assertEqual(self._trace,  [
            ('get-path', v, 'key'),
            ('get-path', v, 'key2'),
            ('get-path', v, 'key3.key4'),
        ])
        self._trace[:] = []

        o["key"] = 42
        o["key3.key4"] = 99
        self.assertEqual(self._trace,  [
            ('set-path', v, 'key', 42),
            ('set-path', v, 'key3.key4', 99),
        ])
        self._trace[:] = []


        self.assertRaises(TypeError, operator.getitem, o, 42)
        self.assertRaises(TypeError, operator.setitem, o, 42, 99)

if __name__ == "__main__":
    main()
