import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

from Quartz import CGSize


class TestCTFramesetter(TestCase):
    def test_types(self):
        self.assertIsInstance(CoreText.CTFramesetterRef, objc.objc_class)

    def test_functions(self):
        v = CoreText.CTFramesetterGetTypeID()
        self.assertIsInstance(v, int)

        setter = CoreText.CTFramesetterCreateWithAttributedString(
            CoreText.CFAttributedStringCreate(None, "hello", None)
        )
        self.assertIsInstance(setter, CoreText.CTFramesetterRef)

        # CTFramesetterCreateFrame: tested in test_ctframe.py

        v = CoreText.CTFramesetterGetTypesetter(setter)
        self.assertIsInstance(v, CoreText.CTTypesetterRef)

    def test_methods(self):
        setter = CoreText.CTFramesetterCreateWithAttributedString(
            CoreText.CFAttributedStringCreate(None, "hello", None)
        )
        self.assertIsInstance(setter, CoreText.CTFramesetterRef)

        self.assertArgIsOut(CoreText.CTFramesetterSuggestFrameSizeWithConstraints, 4)

        r = CoreText.CTFramesetterSuggestFrameSizeWithConstraints(
            setter, CoreText.CFRange(0, 2), None, CGSize(100, 500), None
        )
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)

        size, a_range = r

        self.assertIsInstance(size, CGSize)
        self.assertIsInstance(a_range, CoreText.CFRange)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsCFRetained(CoreText.CTFramesetterCreateWithTypesetter)
