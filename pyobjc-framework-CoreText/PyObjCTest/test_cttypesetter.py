
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTTypesetter (TestCase):
    def testTypes(self):
        self.assertIsCFType(CTTypesetterRef)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCTTypesetterOptionDisableBidiProcessing, unicode)
        self.assertIsInstance(kCTTypesetterOptionForcedEmbeddingLevel, unicode)

    def testFunctions(self):
        self.assertIsInstance(CTTypesetterGetTypeID(), (int, long))

        astring = CFAttributedStringCreate(None, u"hello world", None)
        self.assertIsInstance(astring, CFAttributedStringRef)

        self.assertResultIsCFRetained(CTTypesetterCreateWithAttributedString)
        ref = CTTypesetterCreateWithAttributedString(astring)
        self.assertIsInstance(ref, CTTypesetterRef)

        self.assertResultIsCFRetained(CTTypesetterCreateWithAttributedStringAndOptions)
        options = { 'key': 'value' }
        ref = CTTypesetterCreateWithAttributedStringAndOptions(astring, options)
        self.assertIsInstance(ref, CTTypesetterRef)

        line = CTTypesetterCreateLine(ref, CFRange(0, 5))
        self.assertIsInstance(line, CTLineRef)

        v = CTTypesetterSuggestLineBreak(ref, 0, 100.0)
        self.assertIsInstance(v, (int, long))

        v = CTTypesetterSuggestClusterBreak(ref, 0, 100.0)
        self.assertIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
