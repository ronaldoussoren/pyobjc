from PyObjCTools.TestSupport import *
from CoreText import *
from Foundation import NSDictionary
from Quartz import *

try:
    long
except NameError:
    long = int

class TestCTRunDelegate (TestCase):
    @min_os_level('10.5')
    def testTypes(self):
        self.assertIsCFType(CTRunDelegateRef)

    @min_os_level('10.5')
    def testConstants(self):
        self.assertEqual(kCTRunDelegateVersion1, 1)
        self.assertEqual(kCTRunDelegateCurrentVersion, kCTRunDelegateVersion1)

    @min_os_level('10.5')
    def testFunctions(self):
        self.assertIsInstance(CTRunDelegateGetTypeID(), (int, long))

        self.assertNotIsInstance(CTRunDelegateCreate, objc.function)
        self.assertNotIsInstance(CTRunDelegateGetRefCon, objc.function)

        def getAscender(info):
            return info['ascender']
        def getDescender(info):
            return info['descender']
        def getWidth(info):
            return info['width']

        rc = { 'ascender': 1.0, 'descender': 2.0, 'width': 3.0 }

        o = CTRunDelegateCreate((getAscender, getDescender, getWidth), rc)
        self.assertIsInstance(o, CTRunDelegateRef)

        #v = CTRunDelegateGetRefCon(o)
        #self.assertIs(v, rc)

        # XXX: Still missing tests that actually call the callback
        #      functions.
        self.fail("Tests for using callbacks!")



if __name__ == "__main__":
    main()
