'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
from DictionaryServices import *

class TestDictionaryServices (TestCase):
    def testClasses(self):
        self.failUnless( issubclass(DCSDictionaryRef, objc.lookUpClass('NSCFType')) )
        self.failUnless( DCSDictionaryRef is not objc.lookUpClass('NSCFType') )

    
    def testFunctions(self):
        r = DCSGetTermRangeInString(None, u"the hello world program", 5)
        self.failUnlessIsInstance(r, CFRange)
        self.failUnlessEqual(r, (4, 5))

        r = DCSCopyTextDefinition(None, u"the hello world program", r)
        self.failUnlessIsInstance(r, unicode)


if __name__ == "__main__":
    main()

