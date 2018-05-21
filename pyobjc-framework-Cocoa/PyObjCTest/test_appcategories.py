from PyObjCTools.TestSupport import *
import Cocoa
import PyObjCTools.AppCategories

class TestAppKitCategories (TestCase):
    # XXX: These tests don't actually test anything beyond asserting that
    # the code doesn't crash...

    def testSavedGraphicsState(self):
        with Cocoa.NSGraphicsContext.savedGraphicsState():
            pass

    @onlyIf(hasattr(Cocoa, 'NSAnimationContext'), "Test for NSAnimationContext category")
    def testAnimationContext(self):
        with Cocoa.NSAnimationContext:
            pass

if __name__ == "__main__":
    main()
