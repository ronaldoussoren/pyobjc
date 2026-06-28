import CoreText
from PyObjCTools.TestSupport import TestCase


class TestCTTypesetter(TestCase):
    def test_constants(self):
        self.assertIsInstance(CoreText.kCTTypesetterOptionDisableBidiProcessing, str)
        self.assertIsInstance(CoreText.kCTTypesetterOptionForcedEmbeddingLevel, str)
        self.assertIsInstance(CoreText.kCTTypesetterOptionAllowUnboundedLayout, str)

    def test_types(self):
        self.assertIsCFType(CoreText.CTTypesetterRef)

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

        self.assertResultIsCFRetained(CoreText.CTTypesetterCreateLineWithOffset)
        CoreText.CTTypesetterSuggestLineBreakWithOffset
        CoreText.CTTypesetterSuggestLineBreak
        CoreText.CTTypesetterSuggestClusterBreakWithOffset
