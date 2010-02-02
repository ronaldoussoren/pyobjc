from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSRulerMarker (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSRulerMarker.isMovable)
        self.assertArgIsBOOL(NSRulerMarker.setMovable_, 0)
        self.assertResultIsBOOL(NSRulerMarker.isRemovable)
        self.assertArgIsBOOL(NSRulerMarker.setRemovable_, 0)
        self.assertResultIsBOOL(NSRulerMarker.isDragging)
        self.assertResultIsBOOL(NSRulerMarker.trackMouse_adding_)
        self.assertArgIsBOOL(NSRulerMarker.trackMouse_adding_, 1)

if __name__ == "__main__":
    main()
