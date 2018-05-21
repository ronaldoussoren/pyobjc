from PyObjCTools.TestSupport import *
import Cocoa
import PyObjCTools.FndCategories

class TestFndKitCategories (TestCase):
    # XXX: These tests don't actually test anything beyond asserting that
    # the code doesn't crash...

    def testNSAffineTransform(self):
        t = Cocoa.NSAffineTransform.alloc().init()
        t.rotateByDegrees_atPoint_(40, Cocoa.NSPoint(1, 2))

        t.rotateByRadians_atPoint_(2.5, Cocoa.NSPoint(2.5, 3.5))

if __name__ == "__main__":
    main()
