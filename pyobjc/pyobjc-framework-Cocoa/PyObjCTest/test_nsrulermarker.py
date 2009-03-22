from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSRulerMarker (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSRulerMarker.isMovable)
        self.failUnlessArgIsBOOL(NSRulerMarker.setMovable_, 0)
        self.failUnlessResultIsBOOL(NSRulerMarker.isRemovable)
        self.failUnlessArgIsBOOL(NSRulerMarker.setRemovable_, 0)
        self.failUnlessResultIsBOOL(NSRulerMarker.isDragging)
        self.failUnlessResultIsBOOL(NSRulerMarker.trackMouse_adding_)
        self.failUnlessArgIsBOOL(NSRulerMarker.trackMouse_adding_, 1)

if __name__ == "__main__":
    main()
