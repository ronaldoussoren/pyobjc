import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import objc


class TestCTRunDelegate(TestCase):
    @min_os_level("10.9")
    def testTypes(self):
        self.assertIsCFType(CoreText.CTRunDelegateRef)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(CoreText.kCTRunDelegateVersion1, 1)
        self.assertEqual(
            CoreText.kCTRunDelegateCurrentVersion, CoreText.kCTRunDelegateVersion1
        )

    @expectedFailure
    @min_os_level("10.9")
    def testFunctions(self):
        self.assertIsInstance(CoreText.CTRunDelegateGetTypeID(), int)

        self.assertNotIsInstance(CoreText.CTRunDelegateCreate, objc.function)
        self.assertNotIsInstance(CoreText.CTRunDelegateGetRefCon, objc.function)

        def getAscender(info):
            return info["ascender"]

        def getDescender(info):
            return info["descender"]

        def getWidth(info):
            return info["width"]

        rc = {"ascender": 1.0, "descender": 2.0, "width": 3.0}

        o = CoreText.CTRunDelegateCreate((getAscender, getDescender, getWidth), rc)
        self.assertIsInstance(o, CoreText.CTRunDelegateRef)

        # v = CoreText.CTRunDelegateGetRefCon(o)
        # self.assertIs(v, rc)

        # XXX: Still missing tests that actually call the callback
        #      functions.
        self.fail("Tests for using callbacks!")
