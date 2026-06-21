import CoreText
from PyObjCTools.TestSupport import TestCase


class TestCTTextTab(TestCase):
    def test_types(self):
        self.assertIsCFType(CoreText.CTTextTabRef)

    def test_constants(self):
        self.assertIsInstance(CoreText.kCTTabColumnTerminatorsAttributeName, str)

    def test_functions(self):
        self.assertIsInstance(CoreText.CTTextTabGetTypeID(), int)

        tab = CoreText.CTTextTabCreate(
            CoreText.kCTCenterTextAlignment,
            10.5,
            {
                CoreText.kCTTabColumnTerminatorsAttributeName: CoreText.CFCharacterSetCreateWithCharactersInString(
                    None, "."
                )
            },
        )
        self.assertIsInstance(tab, CoreText.CTTextTabRef)

        v = CoreText.CTTextTabGetAlignment(tab)
        self.assertEqual(v, CoreText.kCTCenterTextAlignment)

        v = CoreText.CTTextTabGetLocation(tab)
        self.assertEqual(v, 10.5)

        v = CoreText.CTTextTabGetOptions(tab)
        self.assertIsInstance(v, dict)
