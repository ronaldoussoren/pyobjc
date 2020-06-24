import ScreenSaver
from PyObjCTools.TestSupport import TestCase
import objc


class TestScreenSaver(TestCase):
    def testClasses(self):
        self.assertHasAttr(ScreenSaver, "ScreenSaverDefaults")
        self.assertIsInstance(ScreenSaver.ScreenSaverDefaults, objc.objc_class)

        self.assertHasAttr(ScreenSaver, "ScreenSaverView")
        self.assertIsInstance(ScreenSaver.ScreenSaverView, objc.objc_class)

        self.assertArgIsBOOL(ScreenSaver.ScreenSaverView.initWithFrame_isPreview_, 1)
        self.assertResultIsBOOL(ScreenSaver.ScreenSaverView.isAnimating)
        self.assertResultIsBOOL(ScreenSaver.ScreenSaverView.isPreview)

    def testInlines(self):
        self.assertHasAttr(ScreenSaver, "SSRandomIntBetween")
        self.assertIsInstance(ScreenSaver.SSRandomIntBetween, objc.function)

        self.assertHasAttr(ScreenSaver, "SSCenteredRectInRect")
        self.assertIsInstance(ScreenSaver.SSCenteredRectInRect, objc.function)

        fn = ScreenSaver.SSCenteredRectInRect
        innerRect = ScreenSaver.NSMakeRect(5, 5, 20, 30)
        outerRect = ScreenSaver.NSMakeRect(0, 0, 50, 60)

        res = fn(innerRect, outerRect)
        self.assertIsInstance(res, ScreenSaver.NSRect)
        self.assertEqual(res, ScreenSaver.NSMakeRect(15, 15.0, 20.0, 30.0))

        fn = ScreenSaver.SSRandomFloatBetween
        for _ in range(10):
            r = fn(1.0, 20.5)
            self.assertTrue(1.0 <= r <= 20.5)
            self.assertIsInstance(r, float)

        fn = ScreenSaver.SSRandomIntBetween
        for _ in range(10):
            r = fn(-10, 20)
            self.assertTrue(-10 <= r <= 20)
            self.assertIsInstance(r, int)

        fn = ScreenSaver.SSRandomPointForSizeWithinRect
        r = fn(ScreenSaver.NSMakeSize(10, 10), ScreenSaver.NSMakeRect(20, 20, 100, 100))
        self.assertIsInstance(r, ScreenSaver.NSPoint)
