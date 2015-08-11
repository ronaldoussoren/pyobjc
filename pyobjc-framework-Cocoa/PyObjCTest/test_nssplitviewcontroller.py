
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSSplitViewController (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertResultIsBOOL(NSSplitViewItem.isCollapsed)
        self.assertArgIsBOOL(NSSplitViewItem.setCollapsed_, 0)
        self.assertResultIsBOOL(NSSplitViewItem.canCollapse)
        self.assertArgIsBOOL(NSSplitViewItem.setCanCollapse_, 0)


if __name__ == "__main__":
    main()
