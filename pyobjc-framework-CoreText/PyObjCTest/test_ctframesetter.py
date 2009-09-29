
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTFramesetter (TestCase):

    def testTypes(self):
        self.failUnlessIsInstance(CTFramesetterRef, objc.objc_class)

    def testFunctions(self):
        v = CTFramesetterGetTypeID()
        self.failUnlessIsInstance(v, (int, long))

        setter = CTFramesetterCreateWithAttributedString(
                    CFAttributedStringCreate(None, u"hello", None))
        self.failUnlessIsInstance(setter, CTFramesetterRef)

        # CTFramesetterCreateFrame: tested in test_ctframe.py

        v = CTFramesetterGetTypesetter(setter)
        self.failUnlessIsInstance(v, CTTypesetterRef)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.fail('CTFramesetterSuggestFrameSizeWithConstraints')


if __name__ == "__main__":
    main()
