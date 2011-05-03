from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVBase (TestCase):
    def testStructs(self):
        v = CVSMPTETime()
        self.assertIsInstance(v.subframes, (int, long))
        self.assertIsInstance(v.subframeDivisor, (int, long))
        self.assertIsInstance(v.counter, (int, long))
        self.assertIsInstance(v.type, (int, long))
        self.assertIsInstance(v.flags, (int, long))
        self.assertIsInstance(v.hours, (int, long))
        self.assertIsInstance(v.minutes, (int, long))
        self.assertIsInstance(v.seconds, (int, long))
        self.assertIsInstance(v.frames, (int, long))

        v = CVTime()
        self.assertIsInstance(v.timeValue, (int, long))
        self.assertIsInstance(v.timeScale, (int, long))
        self.assertIsInstance(v.flags, (int, long))

        v = CVTimeStamp()
        self.assertIsInstance(v.version, (int, long))
        self.assertIsInstance(v.videoTimeScale, (int, long))
        self.assertIsInstance(v.videoTime, (int, long))
        self.assertIsInstance(v.hostTime, (int, long))
        self.assertIsInstance(v.rateScalar, float)
        self.assertIsInstance(v.videoRefreshPeriod, (int, long))
        self.assertIsInstance(v.smpteTime, CVSMPTETime)
        self.assertIsInstance(v.flags, (int, long))
        self.assertIsInstance(v.reserved, (int, long))


    def testConstants(self):
        self.assertEqual(kCVSMPTETimeType24, 0)
        self.assertEqual(kCVSMPTETimeType25, 1)
        self.assertEqual(kCVSMPTETimeType30Drop, 2)
        self.assertEqual(kCVSMPTETimeType30, 3)
        self.assertEqual(kCVSMPTETimeType2997, 4)
        self.assertEqual(kCVSMPTETimeType2997Drop, 5)
        self.assertEqual(kCVSMPTETimeType60, 6)
        self.assertEqual(kCVSMPTETimeType5994, 7)

        self.assertEqual(kCVSMPTETimeValid, 1)
        self.assertEqual(kCVSMPTETimeRunning, 2)

        self.assertEqual(kCVTimeIsIndefinite, 1)

        self.assertEqual(kCVTimeStampVideoTimeValid, 1)
        self.assertEqual(kCVTimeStampHostTimeValid, 2)
        self.assertEqual(kCVTimeStampSMPTETimeValid, 4)
        self.assertEqual(kCVTimeStampVideoRefreshPeriodValid, 8)
        self.assertEqual(kCVTimeStampRateScalarValid, 16)
        self.assertEqual(kCVTimeStampTopField, 1<<16)
        self.assertEqual(kCVTimeStampBottomField, 1<<17)

        self.assertEqual(kCVTimeStampVideoHostTimeValid, (kCVTimeStampVideoTimeValid | kCVTimeStampHostTimeValid))
        self.assertEqual(kCVTimeStampIsInterlaced, (kCVTimeStampTopField | kCVTimeStampBottomField))

        self.assertIsInstance(kCVZeroTime, CVTime)
        self.assertIsInstance(kCVIndefiniteTime, CVTime)



if __name__ == "__main__":
    main()
