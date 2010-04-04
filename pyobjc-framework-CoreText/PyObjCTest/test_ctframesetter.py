
from PyObjCTools.TestSupport import *
from CoreText import *

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
    def testMethods10_5(self):
        self.fail('CTFramesetterSuggestFrameSizeWithConstraints')


if __name__ == "__main__":
    main()
