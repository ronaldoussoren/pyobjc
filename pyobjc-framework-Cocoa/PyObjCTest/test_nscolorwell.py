import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSColorWell(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AppKit.NSColorWellStyle)
        self.assertEqual(AppKit.NSColorWellStyleDefault, 0)
        self.assertEqual(AppKit.NSColorWellStyleMinimal, 1)
        self.assertEqual(AppKit.NSColorWellStyleExpanded, 2)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSColorWell.isActive)
        self.assertArgIsBOOL(AppKit.NSColorWell.activate_, 0)
        self.assertResultIsBOOL(AppKit.NSColorWell.isBordered)
        self.assertArgIsBOOL(AppKit.NSColorWell.setBordered_, 0)

    @min_os_level("13.0")
    def testMethods13_0(self):
        pass
        # self.assertResultIsSEL(AppKit.NSColorWell.pulldownAction, b"v@:@")
