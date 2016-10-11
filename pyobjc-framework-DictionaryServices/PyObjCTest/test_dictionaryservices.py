'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
from DictionaryServices import *

class TestDictionaryServices (TestCase):
    def testClasses(self):
        self.assertIsCFType(DCSDictionaryRef)


    def testFunctions(self):
        txt = b"the hello world program".decode('latin1')
        print(1, repr(txt))
        r = DCSGetTermRangeInString(None, txt, 5)
        print(2)
        self.assertIsInstance(r, CFRange)
        print(3)
        self.assertEqual(r, (4, 5))

        print(4)
        r = DCSCopyTextDefinition(None, txt, r)
        print(5)
        self.assertIsInstance(r, (unicode, type(None)))
        print(6)

        v = DCSDictionaryGetTypeID()
        print(7)
        self.assertIsInstance(v, (int, long))     
        print(8)


if __name__ == "__main__":
    main()
