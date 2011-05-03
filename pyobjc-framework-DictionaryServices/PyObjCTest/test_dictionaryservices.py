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
        r = DCSGetTermRangeInString(None, u"the hello world program", 5)
        self.assertIsInstance(r, CFRange)
        self.assertEqual(r, (4, 5))

        r = DCSCopyTextDefinition(None, u"the hello world program", r)
        self.assertIsInstance(r, unicode)

        v = DCSDictionaryGetTypeID()
        self.assertIsInstance(v, (int, long))


if __name__ == "__main__":
    main()

