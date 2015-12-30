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
        self.assertEqual(NSStackViewSpacingUseDefault, objc._FLT_MAX)

        self.assertEqual(NSStackViewDistributionGravityAreas, -1)
        self.assertEqual(NSStackViewDistributionFill, 0)
        self.assertEqual(NSStackViewDistributionFillEqually, 1)
        self.assertEqual(NSStackViewDistributionFillProportionally, 2)
        self.assertEqual(NSStackViewDistributionEqualSpacing, 3)
        self.assertEqual(NSStackViewDistributionEqualCentering, 4)

    @min_os_level('10.9')
    def testMethods(self):
        self.assertResultIsBOOL(NSStackView.hasEqualSpacing)
        self.assertArgIsBOOL(NSStackView.setHasEqualSpacing_, 0)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(NSStackView.detachesHiddenViews)
        self.assertArgIsBOOL(NSStackView.setDetachesHiddenViews_, 0)

    @min_sdk_level('10.10')
    def testProtocolObjects(self):
        objc.protocolNamed('NSStackViewDelegate')


if __name__ == "__main__":
    main()
