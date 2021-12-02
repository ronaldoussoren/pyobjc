from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCVBase(TestCase):
    def testStructs(self):
        v = Quartz.CVSMPTETime()
        self.assertIsInstance(v.subframes, int)
        self.assertIsInstance(v.subframeDivisor, int)
        self.assertIsInstance(v.counter, int)
        self.assertIsInstance(v.type, int)
        self.assertIsInstance(v.flags, int)
        self.assertIsInstance(v.hours, int)
        self.assertIsInstance(v.minutes, int)
        self.assertIsInstance(v.seconds, int)
        self.assertIsInstance(v.frames, int)
        self.assertPickleRoundTrips(v)

        v = Quartz.CVTime()
        self.assertIsInstance(v.timeValue, int)
        self.assertIsInstance(v.timeScale, int)
        self.assertIsInstance(v.flags, int)
        self.assertPickleRoundTrips(v)

        v = Quartz.CVTimeStamp()
        self.assertIsInstance(v.version, int)
        self.assertIsInstance(v.videoTimeScale, int)
        self.assertIsInstance(v.videoTime, int)
        self.assertIsInstance(v.hostTime, int)
        self.assertIsInstance(v.rateScalar, float)
        self.assertIsInstance(v.videoRefreshPeriod, int)
        self.assertIsInstance(v.smpteTime, Quartz.CVSMPTETime)
        self.assertIsInstance(v.flags, int)
        self.assertIsInstance(v.reserved, int)
        self.assertPickleRoundTrips(v)

    def testConstants(self):
        self.assertEqual(Quartz.kCVSMPTETimeType24, 0)
        self.assertEqual(Quartz.kCVSMPTETimeType25, 1)
        self.assertEqual(Quartz.kCVSMPTETimeType30Drop, 2)
        self.assertEqual(Quartz.kCVSMPTETimeType30, 3)
        self.assertEqual(Quartz.kCVSMPTETimeType2997, 4)
        self.assertEqual(Quartz.kCVSMPTETimeType2997Drop, 5)
        self.assertEqual(Quartz.kCVSMPTETimeType60, 6)
        self.assertEqual(Quartz.kCVSMPTETimeType5994, 7)

        self.assertEqual(Quartz.kCVSMPTETimeValid, 1)
        self.assertEqual(Quartz.kCVSMPTETimeRunning, 2)

        self.assertEqual(Quartz.kCVTimeIsIndefinite, 1)

        self.assertEqual(Quartz.kCVTimeStampVideoTimeValid, 1)
        self.assertEqual(Quartz.kCVTimeStampHostTimeValid, 2)
        self.assertEqual(Quartz.kCVTimeStampSMPTETimeValid, 4)
        self.assertEqual(Quartz.kCVTimeStampVideoRefreshPeriodValid, 8)
        self.assertEqual(Quartz.kCVTimeStampRateScalarValid, 16)
        self.assertEqual(Quartz.kCVTimeStampTopField, 1 << 16)
        self.assertEqual(Quartz.kCVTimeStampBottomField, 1 << 17)

        self.assertEqual(
            Quartz.kCVTimeStampVideoHostTimeValid,
            (Quartz.kCVTimeStampVideoTimeValid | Quartz.kCVTimeStampHostTimeValid),
        )
        self.assertEqual(
            Quartz.kCVTimeStampIsInterlaced,
            (Quartz.kCVTimeStampTopField | Quartz.kCVTimeStampBottomField),
        )

        self.assertIsInstance(Quartz.kCVZeroTime, Quartz.CVTime)
        self.assertIsInstance(Quartz.kCVIndefiniteTime, Quartz.CVTime)
