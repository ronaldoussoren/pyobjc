
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAMediaTimingHelper (NSObject, objc.protocolNamed('CAMediaTiming')):
    def beginTime(self): return 1
    def setBeginTime_(self, v): pass
    def duration(self): return 1
    def setDuration_(self, v): pass
    def speed(self): return 1
    def setSpeed_(self, v): pass
    def timeOffset(self): return 1
    def setTimeOffset_(self, v): pass
    def repeatCount(self): return 1
    def setRepeatCount_(self, v): pass
    def repeatDuration(self): return 1
    def setRepeatDuration_(self, v): pass
    def autoreverses(self): return 1
    def setAutoreverses_(self, v): return 1
    def fillMode(self): return 1
    def setFillMode_(self, v): pass

class TestCAMediaTiming (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCAFillModeForwards, unicode)
        self.failUnlessIsInstance(kCAFillModeBackwards, unicode)
        self.failUnlessIsInstance(kCAFillModeBoth, unicode)
        self.failUnlessIsInstance(kCAFillModeRemoved, unicode)

    def testMethods(self):
        self.failUnlessResultHasType(TestCAMediaTimingHelper.beginTime, objc._C_DBL)
        self.failUnlessArgHasType(TestCAMediaTimingHelper.setBeginTime_, 0, objc._C_DBL)
        self.failUnlessResultHasType(TestCAMediaTimingHelper.duration, objc._C_DBL)
        self.failUnlessArgHasType(TestCAMediaTimingHelper.setDuration_, 0, objc._C_DBL)
        self.failUnlessResultHasType(TestCAMediaTimingHelper.speed, objc._C_FLT)
        self.failUnlessArgHasType(TestCAMediaTimingHelper.setSpeed_, 0, objc._C_FLT)
        self.failUnlessResultHasType(TestCAMediaTimingHelper.timeOffset, objc._C_DBL)
        self.failUnlessArgHasType(TestCAMediaTimingHelper.setTimeOffset_, 0, objc._C_DBL)
        self.failUnlessResultHasType(TestCAMediaTimingHelper.repeatCount, objc._C_FLT)
        self.failUnlessArgHasType(TestCAMediaTimingHelper.setRepeatCount_, 0, objc._C_FLT)
        self.failUnlessResultHasType(TestCAMediaTimingHelper.repeatDuration, objc._C_DBL)
        self.failUnlessArgHasType(TestCAMediaTimingHelper.setRepeatDuration_, 0, objc._C_DBL)
        self.failUnlessResultHasType(TestCAMediaTimingHelper.autoreverses, objc._C_NSBOOL)
        self.failUnlessArgHasType(TestCAMediaTimingHelper.setAutoreverses_, 0, objc._C_NSBOOL)
        self.failUnlessResultHasType(TestCAMediaTimingHelper.fillMode, objc._C_ID)
        self.failUnlessArgHasType(TestCAMediaTimingHelper.setFillMode_, 0, objc._C_ID)


if __name__ == "__main__":
    main()
