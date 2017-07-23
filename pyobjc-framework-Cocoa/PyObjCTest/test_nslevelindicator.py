from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSLevelIndicator (TestCase):
    def testConstants(self):
        self.assertEqual(NSLevelIndicatorPlaceholderVisibilityAutomatic, 0)
        self.assertEqual(NSLevelIndicatorPlaceholderVisibilityAlways, 1)
        self.assertEqual(NSLevelIndicatorPlaceholderVisibilityWhileEditing, 2)

    @min_os_level('10.13')
    def testMethods(self):
        self.assertResultIsBOOL(NSLevelIndicator.drawsTieredCapacityLevels)
        self.assertArgIsBOOL(NSLevelIndicator.setDrawsTieredCapacityLevels_, 0)

        self.assertResultIsBOOL(NSLevelIndicator.isEditable)
        self.assertArgIsBOOL(NSLevelIndicator.setEditable_, 0)

if __name__ == "__main__":
    main()
