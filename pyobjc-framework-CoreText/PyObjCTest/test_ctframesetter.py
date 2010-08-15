
from PyObjCTools.TestSupport import *
from CoreText import *

try:
    from Quartz import CGSize
except ImportError:
    CGSize = None, None


class TestCTFramesetter (TestCase):

    def testTypes(self):
        self.assertIsInstance(CTFramesetterRef, objc.objc_class)

    def testFunctions(self):
        v = CTFramesetterGetTypeID()
        self.assertIsInstance(v, (int, long))

        setter = CTFramesetterCreateWithAttributedString(
                    CFAttributedStringCreate(None, u"hello", None))
        self.assertIsInstance(setter, CTFramesetterRef)

        # CTFramesetterCreateFrame: tested in test_ctframe.py

        v = CTFramesetterGetTypesetter(setter)
        self.assertIsInstance(v, CTTypesetterRef)

    @min_os_level('10.5')
    @onlyIf(CGSize is not None, "CoreGraphics not available")
    def testMethods10_5(self):
        #self.fail('CTFramesetterSuggestFrameSizeWithConstraints')
        setter = CTFramesetterCreateWithAttributedString(
                    CFAttributedStringCreate(None, u"hello", None))
        self.assertIsInstance(setter, CTFramesetterRef)

        self.assertArgIsOut(CTFramesetterSuggestFrameSizeWithConstraints, 4)

        r = CTFramesetterSuggestFrameSizeWithConstraints(
                setter, CFRange(0, 2), None, CGSize(100, 500),
                None)
        self.assertIsInstance(r, tuple)
        self.assertEquals(len(r), 2)

        size, range = r

        self.assertIsInstance(size, CGSize)
        self.assertIsInstance(range, CFRange)



if __name__ == "__main__":
    main()
