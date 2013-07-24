from PyObjCTools.TestSupport import *
import objc
import objc._convenience as convenience

class TestNSData (TestCase):
    def test_creation(self):
        NSData = objc.lookUpClass('NSData')
        NSMutableData = objc.lookUpClass('NSMutableData')

        data = NSData(b'hello')
        data2 = NSMutableData(b'moon')

        self.assertEqual(bytes(data), b'hello')
        self.assertEqual(bytes(data2), b'moon')

        self.assertIsInstance(data, NSData)
        self.assertIsInstance(data2, NSMutableData)

    def test_to_string(self):
        NSData = objc.lookUpClass('NSData')

        data = NSData(b'hello')
        data2 = NSData()

        self.assertEqual(str(data), str(b'hello'))
        self.assertEqual(str(data2), str(b''))

    def reading(self):
        NSData = objc.lookUpClass('NSData')
        bdata = b'hello'
        data = NSData(bdata)

        self.assertEqual(data[0], bdata[0])
        self.assertEqual(data[0:2], bdata[0:2])
        self.assertEqual(data[0:6:2], bdata[0:6:2])

    def writing(self):
        NSData = objc.lookUpClass('NSMutableData')
        bdata = b'hello'
        data = NSData(bdata)
        barray = bytearray(bdata)

        bdata[0] = b'x'[0]
        barray[0] = b'x'[0]
        self.assertEqual(bytes(bdata), bytes(barray))

        bdata[0:2] = b'..'
        barray[0:2] = b'..'
        self.assertEqual(bytes(bdata), bytes(barray))

        bdata[0:4:2] = b'++'
        barray[0:4:2] = b'++'
        self.assertEqual(bytes(bdata), bytes(barray))

        for idx in range(len(barray)):
            self.assertEqual(barray[idx], bdata[idx])

        try:
            barray[0:4:2] = b'----'
            self.fail("Exception not raised")
        except ValueError:
            pass

        try:
            bdata[0:4:2] = b'----'
            self.fail("Exception not raised")
        except ValueError:
            pass

        # XXX: more testing needed?

class TestNULLConvenience(TestCase):
    def test_nsnull(self):
        NSNull = objc.lookUpClass('NSNull')
        null = NSNull.null()
        self.assertFalse(null)

class TestNSString (TestCase):
    def test_nsstring_creation(self):
        NSString = objc.lookUpClass('NSString')

        value = NSString('hello world')
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(value, 'hello world')
        self.assertIsInstance(value.nsstring(), NSString)

        value = NSString()
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(value, '')
        self.assertIsInstance(value.nsstring(), NSString)

    def test_nsstring_creation(self):
        NSMutableString = objc.lookUpClass('NSMutableString')

        value = NSMutableString('hello world')
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(value, 'hello world')
        self.assertIsInstance(value.nsstring(), NSMutableString)

        value = NSMutableString()
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(value, '')
        self.assertIsInstance(value.nsstring(), NSMutableString)

    def test_apis(self):
        NSMutableString = objc.lookUpClass('NSMutableString')

        value = NSMutableString('hello world')
        self.assertIsNotInstance(value, NSMutableString)
        value = value.nsstring()
        self.assertIsInstance(value, NSMutableString)

        self.assertEqual(len(value), 11)
        self.assertFalse(value.startswith('Hello'))
        self.assertTrue(value.startswith('hello'))
        self.assertFalse(value.endswith('moon'))
        self.assertTrue(value.endswith('orld'))

class TestConvenienceHelpers (TestCase):
    def test_add_for_class(self):
        self.assertNotIn("MyObject", convenience.CLASS_METHODS)

        methods = [
            ('info', lambda self: self.description())
        ]

        try:
            objc.addConvenienceForClass("MyObject", methods)
            self.assertEqual(convenience.CLASS_METHODS["MyObject"], tuple(methods))

        finally:
            if 'MyObject' in convenience.CLASS_METHODS:
                del convenience.CLASS_METHODS["MyObject"]



class TestBasicConveniences (TestCase):
    def testBundleForClass(self):
        orig = convenience.currentBundle
        try:
            the_bundle = object()
            def currentBundle():
                return the_bundle
            convenience.currentBundle = currentBundle

            class OC_Test_Basic_Convenience_1 (objc.lookUpClass("NSObject")):
                pass

            self.assertIs(OC_Test_Basic_Convenience_1.bundleForClass(), the_bundle)
        finally:
            convenience.currentBundle = orig

    def test_kvc_helper(self):
        o = objc.lookUpClass('NSURL').URLWithString_('http://www.python.org/')
        self.assertEqual(o.host(), 'www.python.org')

        self.assertEqual(o._.host, 'www.python.org')
        self.assertEqual(o._['host'], 'www.python.org')
        self.assertRaises(TypeError, lambda: o._[42])
        self.assertEqual(repr(o._), '<KVC accessor for %r>'%(o,))
        self.assertRaises(AttributeError, getattr, o._, 'nosuchattr')
        self.assertRaises(TypeError, o._.__setitem__, 42)

        o = objc.lookUpClass('NSMutableDictionary').dictionary()
        o._.key1 = 1
        o._['key2'] = 2

        self.assertEqual(o, {'key1': 1, 'key2': 2 })
        self.assertRaises(AttributeError, o._.nosuchattr)
        self.assertRaises(TypeError, o._.__setitem__, 42)


if __name__ == "__main__":
    main()
