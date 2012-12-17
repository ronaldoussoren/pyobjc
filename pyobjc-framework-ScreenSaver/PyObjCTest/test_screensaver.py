'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import ScreenSaver

try:
    long
except NameError:
    long = int

class TestScreenSaver (TestCase):
    def testClasses(self):
        self.assertHasAttr(ScreenSaver, 'ScreenSaverDefaults')
        self.assertIsInstance(ScreenSaver.ScreenSaverDefaults, objc.objc_class)

        self.assertHasAttr(ScreenSaver, 'ScreenSaverView')
        self.assertIsInstance(ScreenSaver.ScreenSaverView, objc.objc_class)

    def testInlines(self):
        self.assertHasAttr(ScreenSaver, 'SSRandomIntBetween')
        self.assertIsInstance(ScreenSaver.SSRandomIntBetween, objc.function)

        self.assertHasAttr(ScreenSaver, 'SSCenteredRectInRect')
        self.assertIsInstance(ScreenSaver.SSCenteredRectInRect, objc.function)

        fn = ScreenSaver.SSCenteredRectInRect
        innerRect = ScreenSaver.NSMakeRect(5, 5, 20, 30)
        outerRect = ScreenSaver.NSMakeRect(0, 0, 50, 60)

        res = fn(innerRect, outerRect)
        self.assert_(isinstance(res, ScreenSaver.NSRect))
        self.assertEquals(res, ScreenSaver.NSMakeRect(15, 15.0, 20.0, 30.0))

        fn = ScreenSaver.SSRandomFloatBetween
        for _ in range(10):
            r = fn(1.0, 20.5)
            self.assert_(1.0 <= r <= 20.5)
            self.assert_(isinstance(r, float))

        fn = ScreenSaver.SSRandomIntBetween
        for _ in range(10):
            r = fn(-10, 20)
            self.assert_(-10 <= r <= 20)
            self.assert_(isinstance(r, (int, long)))

        fn = ScreenSaver.SSRandomPointForSizeWithinRect
        r = fn(ScreenSaver.NSMakeSize(10, 10), ScreenSaver.NSMakeRect(20, 20, 100, 100))
        self.assert_(isinstance(r, ScreenSaver.NSPoint))


if __name__ == "__main__":
    main()
