from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStackView (TestCase):
    def testConstants(self):
        self.assertEqual(NSUserInterfaceLayoutOrientationHorizontal, 0)
        self.assertEqual(NSUserInterfaceLayoutOrientationVertical, 1)

        self.assertEqual(NSStackViewGravityTop, 1)
        self.assertEqual(NSStackViewGravityLeading, 1)
        self.assertEqual(NSStackViewGravityCenter, 2)
        self.assertEqual(NSStackViewGravityBottom, 3)
        self.assertEqual(NSStackViewGravityTrailing, 3)

        self.assertEqual(NSStackViewVisibilityPriorityMustHold, 1000.0)
        self.assertEqual(NSStackViewVisibilityPriorityDetachOnlyIfNecessary, 900.0)
        self.assertEqual(NSStackViewVisibilityPriorityNotVisible, 0.0)

        self.assertIsInstance(NSStackViewSpacingUseDefault, float)

    @min_os_level('10.9')
    def testMethods(self):
        self.assertResultIsBOOL(NSStackView.hasEqualSpacing)
        self.assertArgIsBOOL(NSStackView.setHasEqualSpacing_, 0)

    @min_sdk_level('10.9')
    def testProtocols(self):
        objc.protocolNamed('NSStackViewDelegate')


if __name__ == "__main__":
    main()
