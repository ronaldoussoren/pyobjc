from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSScrubberItemView (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(NSScrubberArrangedView.isSelected)
        self.assertArgIsBOOL(NSScrubberArrangedView.setSelected_, 0)

        self.assertResultIsBOOL(NSScrubberArrangedView.isHighlighted)
        self.assertArgIsBOOL(NSScrubberArrangedView.setHighlighted_, 0)

if __name__ == "__main__":
    main()
