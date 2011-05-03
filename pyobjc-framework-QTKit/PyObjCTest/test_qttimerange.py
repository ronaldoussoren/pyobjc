
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTTimeRange (TestCase):
    def testStructs(self):
        v = QTTimeRange()
        self.assertHasAttr(v, 'time')
        self.assertHasAttr(v, 'duration')

    def testFunctions(self):
        v = QTMakeTimeWithTimeInterval(1500.0)
        w = QTMakeTimeWithTimeInterval(10.0)

        rng = QTMakeTimeRange(v, w)
        self.assertIsInstance(rng, QTTimeRange)

        rng2 = QTMakeTimeRange(w, v)
        self.assertIsInstance(rng2, QTTimeRange)

        self.assertResultIsBOOL(QTTimeInTimeRange)
        self.assertResultIsBOOL(QTEqualTimeRanges)

        o = QTTimeInTimeRange(v, rng)
        self.assertTrue(o is True)
        o = QTTimeInTimeRange(w, rng)
        self.assertTrue(o is False)

        o = QTEqualTimeRanges(rng, rng)
        self.assertTrue(o is True)

        o = QTTimeRangeEnd(rng)
        self.assertIsInstance(o, QTTime)

        o = QTUnionTimeRange(rng, rng2)
        self.assertIsInstance(o, QTTimeRange)

        o = QTIntersectionTimeRange(rng, rng2)
        self.assertIsInstance(o, QTTimeRange)

if __name__ == "__main__":
    main()
