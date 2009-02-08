
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTTextTab (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CTTextTabRef)

    def testConstants(self):
        self.failUnlessIsInstance(kCTTabColumnTerminatorsAttributeName, unicode)

    def testFunctions(self):
        self.failUnlessIsInstance(CTTextTabGetTypeID(), (int, long))

        tab = CTTextTabCreate(kCTCenterTextAlignment, 10.5, { u"key": u"value" })
        self.failUnlessIsInstance(tab, CTTextTabRef)

        v = CTTextTabGetAlignment(tab)
        self.failUnlessEqual(v , kCTCenterTextAlignment)

        v = CTTextTabGetLocation(tab)
        self.failUnlessEqual(v , 10.5)

        v = CTTextTabGetOptions(tab)
        self.failUnlessIsInstance(v, dict)


if __name__ == "__main__":
    main()
