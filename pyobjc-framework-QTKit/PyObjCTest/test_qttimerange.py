from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTTimeRange(TestCase):
    def testStructs(self):
        v = QTKit.QTTimeRange()
        self.assertHasAttr(v, "time")
        self.assertHasAttr(v, "duration")

    def testFunctions(self):
        v = QTKit.QTMakeTimeWithTimeInterval(1500.0)
        w = QTKit.QTMakeTimeWithTimeInterval(10.0)

        rng = QTKit.QTMakeTimeRange(v, w)
        self.assertIsInstance(rng, QTKit.QTTimeRange)

        rng2 = QTKit.QTMakeTimeRange(w, v)
        self.assertIsInstance(rng2, QTKit.QTTimeRange)

        self.assertResultIsBOOL(QTKit.QTTimeInTimeRange)
        self.assertResultIsBOOL(QTKit.QTEqualTimeRanges)

        o = QTKit.QTTimeInTimeRange(v, rng)
        self.assertTrue(o is True)
        o = QTKit.QTTimeInTimeRange(w, rng)
        self.assertTrue(o is False)

        o = QTKit.QTEqualTimeRanges(rng, rng)
        self.assertTrue(o is True)

        o = QTKit.QTTimeRangeEnd(rng)
        self.assertIsInstance(o, QTKit.QTTime)

        o = QTKit.QTUnionTimeRange(rng, rng2)
        self.assertIsInstance(o, QTKit.QTTimeRange)

        o = QTKit.QTIntersectionTimeRange(rng, rng2)
        self.assertIsInstance(o, QTKit.QTTimeRange)

        s = QTKit.QTStringFromTimeRange(rng)
        self.assertIsInstance(s, str)

        t = QTKit.QTTimeRangeFromString(s)
        self.assertIsInstance(t, QTKit.QTTimeRange)

        self.assertTrue(QTKit.QTEqualTimeRanges(t, rng))
