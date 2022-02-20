import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTextSelection(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTextSelectionAffinity)
        self.assertIsEnumType(AppKit.NSTextSelectionGranularity)

    def test_constants(self):
        self.assertEqual(AppKit.NSTextSelectionGranularityCharacter, 0)
        self.assertEqual(AppKit.NSTextSelectionGranularityWord, 1)
        self.assertEqual(AppKit.NSTextSelectionGranularityParagraph, 2)
        self.assertEqual(AppKit.NSTextSelectionGranularityLine, 3)
        self.assertEqual(AppKit.NSTextSelectionGranularitySentence, 4)

        self.assertEqual(AppKit.NSTextSelectionAffinityUpstream, 0)
        self.assertEqual(AppKit.NSTextSelectionAffinityDownstream, 1)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(AppKit.NSTextSelection.isTransient)
        self.assertResultIsBOOL(AppKit.NSTextSelection.isLogical)
