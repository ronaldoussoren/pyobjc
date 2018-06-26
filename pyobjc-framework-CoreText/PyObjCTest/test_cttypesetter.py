
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTTypesetter (TestCase):
    def testTypes(self):
        self.assertIsCFType(CTTypesetterRef)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCTTypesetterOptionDisableBidiProcessing, unicode)
        self.assertIsInstance(kCTTypesetterOptionForcedEmbeddingLevel, unicode)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(kCTTypesetterOptionAllowUnboundedLayout, unicode)

    def testFunctions(self):
        self.assertIsInstance(CTTypesetterGetTypeID(), (int, long))

        astring = CFAttributedStringCreate(None, b"hello world".decode('latin1'), None)
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

    @min_os_level('10.7')
    def testFunctions10_6(self):
	# FIXME: For some reason these aren't avaible on OSX 10.6...
        self.assertResultIsCFRetained(CTTypesetterCreateLineWithOffset)
        CTTypesetterSuggestLineBreakWithOffset
        CTTypesetterSuggestLineBreak
        CTTypesetterSuggestClusterBreakWithOffset


if __name__ == "__main__":
    main()
