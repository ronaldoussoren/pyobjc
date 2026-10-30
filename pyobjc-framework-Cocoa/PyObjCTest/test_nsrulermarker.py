import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSRulerMarker(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSRulerMarker.isMovable)
        self.assertArgIsBOOL(AppKit.NSRulerMarker.setMovable_, 0)
        self.assertResultIsBOOL(AppKit.NSRulerMarker.isRemovable)
        self.assertArgIsBOOL(AppKit.NSRulerMarker.setRemovable_, 0)
        self.assertResultIsBOOL(AppKit.NSRulerMarker.isDragging)
        self.assertResultIsBOOL(AppKit.NSRulerMarker.trackMouse_adding_)
        self.assertArgIsBOOL(AppKit.NSRulerMarker.trackMouse_adding_, 1)
