from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSRuleMarker (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSRuleMarker.isMovable)
        self.assertArgIsBOOL(NSRuleMarker.setMovable_, 0)

        self.assertResultIsBOOL(NSRuleMarker.isRemovable)
        self.assertArgIsBOOL(NSRuleMarker.setRemovable_, 0)

        self.assertResultIsBOOL(NSRuleMarker.isDragging)

        self.assertResultIsBOOL(NSRuleMarker.trackMouse_adding_)
        self.assertArgIsBOOL(NSRuleMarker.trackMouse_adding_, 1)

if __name__ == "__main__":
    main()
