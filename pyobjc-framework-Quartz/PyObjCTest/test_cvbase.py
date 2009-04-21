from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVBase (TestCase):
    def testStructs(self):
        v = CVSMPTETime()
        self.failUnlessIsInstance(v.subframes, (int, long))
        self.failUnlessIsInstance(v.subframeDivisor, (int, long))
        self.failUnlessIsInstance(v.counter, (int, long))
        self.failUnlessIsInstance(v.type, (int, long))
        self.failUnlessIsInstance(v.flags, (int, long))
        self.failUnlessIsInstance(v.hours, (int, long))
        self.failUnlessIsInstance(v.minutes, (int, long))
        self.failUnlessIsInstance(v.seconds, (int, long))
        self.failUnlessIsInstance(v.frames, (int, long))

        v = CVTime()
        self.failUnlessIsInstance(v.timeValue, (int, long))
        self.failUnlessIsInstance(v.timeScale, (int, long))
        self.failUnlessIsInstance(v.flags, (int, long))

        v = CVTimeStamp()
        self.failUnlessIsInstance(v.version, (int, long))
        self.failUnlessIsInstance(v.videoTimeScale, (int, long))
        self.failUnlessIsInstance(v.videoTime, (int, long))
        self.failUnlessIsInstance(v.hostTime, (int, long))
        self.failUnlessIsInstance(v.rateScalar, float)
        self.failUnlessIsInstance(v.videoRefreshPeriod, (int, long))
        self.failUnlessIsInstance(v.smpteTime, CVSMPTETime)
        self.failUnlessIsInstance(v.flags, (int, long))
        self.failUnlessIsInstance(v.reserved, (int, long))


    def testConstants(self):
        self.failUnlessEqual(kCVSMPTETimeType24, 0)
        self.failUnlessEqual(kCVSMPTETimeType25, 1)
        self.failUnlessEqual(kCVSMPTETimeType30Drop, 2)
        self.failUnlessEqual(kCVSMPTETimeType30, 3)
        self.failUnlessEqual(kCVSMPTETimeType2997, 4)
        self.failUnlessEqual(kCVSMPTETimeType2997Drop, 5)
        self.failUnlessEqual(kCVSMPTETimeType60, 6)
        self.failUnlessEqual(kCVSMPTETimeType5994, 7)

        self.failUnlessEqual(kCVSMPTETimeValid, 1)
        self.failUnlessEqual(kCVSMPTETimeRunning, 2)

        self.failUnlessEqual(kCVTimeIsIndefinite, 1)

        self.failUnlessEqual(kCVTimeStampVideoTimeValid, 1)
        self.failUnlessEqual(kCVTimeStampHostTimeValid, 2)
        self.failUnlessEqual(kCVTimeStampSMPTETimeValid, 4)
        self.failUnlessEqual(kCVTimeStampVideoRefreshPeriodValid, 8)
        self.failUnlessEqual(kCVTimeStampRateScalarValid, 16)
        self.failUnlessEqual(kCVTimeStampTopField, 1<<16)
        self.failUnlessEqual(kCVTimeStampBottomField, 1<<17)

        self.failUnlessEqual(kCVTimeStampVideoHostTimeValid, (kCVTimeStampVideoTimeValid | kCVTimeStampHostTimeValid))
        self.failUnlessEqual(kCVTimeStampIsInterlaced, (kCVTimeStampTopField | kCVTimeStampBottomField))

        self.failUnlessIsInstance(kCVZeroTime, CVTime)
        self.failUnlessIsInstance(kCVIndefiniteTime, CVTime)



if __name__ == "__main__":
    main()
