import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCTTypesetter(TestCase):
    def test_types(self):
        self.assertIsCFType(CoreText.CTTypesetterRef)

    @min_os_level("10.5")
    def test_constants10_5(self):
        self.assertIsInstance(CoreText.kCTTypesetterOptionDisableBidiProcessing, str)
        self.assertIsInstance(CoreText.kCTTypesetterOptionForcedEmbeddingLevel, str)

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(CoreText.kCTTypesetterOptionAllowUnboundedLayout, str)

    def test_functions(self):
        self.assertIsInstance(CoreText.CTTypesetterGetTypeID(), int)

        astring = CoreText.CFAttributedStringCreate(None, "hello world", None)
        self.assertIsInstance(astring, CoreText.CFAttributedStringRef)

        self.assertResultIsCFRetained(CoreText.CTTypesetterCreateWithAttributedString)
        ref = CoreText.CTTypesetterCreateWithAttributedString(astring)
        self.assertIsInstance(ref, CoreText.CTTypesetterRef)

        self.assertResultIsCFRetained(
            CoreText.CTTypesetterCreateWithAttributedStringAndOptions
        )
        options = {"key": "value"}
        ref = CoreText.CTTypesetterCreateWithAttributedStringAndOptions(
            astring, options
        )
        self.assertIsInstance(ref, CoreText.CTTypesetterRef)

        line = CoreText.CTTypesetterCreateLine(ref, CoreText.CFRange(0, 5))
        self.assertIsInstance(line, CoreText.CTLineRef)

        v = CoreText.CTTypesetterSuggestLineBreak(ref, 0, 100.0)
        self.assertIsInstance(v, int)

        v = CoreText.CTTypesetterSuggestClusterBreak(ref, 0, 100.0)
        self.assertIsInstance(v, int)

    @min_os_level("10.7")
    def test_functions10_6(self):
        # FIXME: For some reason these aren't avaible on OSX 10.6...
        self.assertResultIsCFRetained(CoreText.CTTypesetterCreateLineWithOffset)
        CoreText.CTTypesetterSuggestLineBreakWithOffset
        CoreText.CTTypesetterSuggestLineBreak
        CoreText.CTTypesetterSuggestClusterBreakWithOffset
