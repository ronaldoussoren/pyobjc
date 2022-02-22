from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCAMediaTimingHelper(Quartz.NSObject):
    __pyobjc_protocols__ = [objc.protocolNamed("CAMediaTiming")]

    def beginTime(self):
        return 1

    def setBeginTime_(self, v):
        pass

    def duration(self):
        return 1

    def setDuration_(self, v):
        pass

    def speed(self):
        return 1

    def setSpeed_(self, v):
        pass

    def timeOffset(self):
        return 1

    def setTimeOffset_(self, v):
        pass

    def repeatCount(self):
        return 1

    def setRepeatCount_(self, v):
        pass

    def repeatDuration(self):
        return 1

    def setRepeatDuration_(self, v):
        pass

    def autoreverses(self):
        return 1

    def setAutoreverses_(self, v):
        return 1

    def fillMode(self):
        return 1

    def setFillMode_(self, v):
        pass


class TestCAMediaTiming(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.CAMediaTimingFillMode, str)

    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.kCAFillModeForwards, str)
        self.assertIsInstance(Quartz.kCAFillModeBackwards, str)
        self.assertIsInstance(Quartz.kCAFillModeBoth, str)
        self.assertIsInstance(Quartz.kCAFillModeRemoved, str)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultHasType(TestCAMediaTimingHelper.beginTime, objc._C_DBL)
        self.assertArgHasType(TestCAMediaTimingHelper.setBeginTime_, 0, objc._C_DBL)
        self.assertResultHasType(TestCAMediaTimingHelper.duration, objc._C_DBL)
        self.assertArgHasType(TestCAMediaTimingHelper.setDuration_, 0, objc._C_DBL)
        self.assertResultHasType(TestCAMediaTimingHelper.speed, objc._C_FLT)
        self.assertArgHasType(TestCAMediaTimingHelper.setSpeed_, 0, objc._C_FLT)
        self.assertResultHasType(TestCAMediaTimingHelper.timeOffset, objc._C_DBL)
        self.assertArgHasType(TestCAMediaTimingHelper.setTimeOffset_, 0, objc._C_DBL)
        self.assertResultHasType(TestCAMediaTimingHelper.repeatCount, objc._C_FLT)
        self.assertArgHasType(TestCAMediaTimingHelper.setRepeatCount_, 0, objc._C_FLT)
        self.assertResultHasType(TestCAMediaTimingHelper.repeatDuration, objc._C_DBL)
        self.assertArgHasType(
            TestCAMediaTimingHelper.setRepeatDuration_, 0, objc._C_DBL
        )
        self.assertResultHasType(TestCAMediaTimingHelper.autoreverses, objc._C_NSBOOL)
        self.assertArgHasType(
            TestCAMediaTimingHelper.setAutoreverses_, 0, objc._C_NSBOOL
        )
        self.assertResultHasType(TestCAMediaTimingHelper.fillMode, objc._C_ID)
        self.assertArgHasType(TestCAMediaTimingHelper.setFillMode_, 0, objc._C_ID)

    @min_os_level("10.5")
    def testProtocols(self):
        objc.protocolNamed("CAMediaTiming")
