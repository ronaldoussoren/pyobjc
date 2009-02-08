
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTTimeRange (TestCase):
    def testStructs(self):
        v = QTTimeRange()
        self.failUnless(hasattr(v, 'time'))
        self.failUnless(hasattr(v, 'duration'))

    def testFunctions(self):
        v = QTMakeTimeWithTimeInterval(1500.0)
        w = QTMakeTimeWithTimeInterval(10.0)

        rng = QTMakeTimeRange(v, w)
        self.failUnlessIsInstance(rng, QTTimeRange)

        rng2 = QTMakeTimeRange(w, v)
        self.failUnlessIsInstance(rng2, QTTimeRange)

        self.failUnlessResultIsBOOL(QTTimeInTimeRange)
        self.failUnlessResultIsBOOL(QTEqualTimeRanges)

        o = QTTimeInTimeRange(v, rng)
        self.failUnless(o is True)
        o = QTTimeInTimeRange(w, rng)
        self.failUnless(o is False)

        o = QTEqualTimeRanges(rng, rng)
        self.failUnless(o is True)

        o = QTTimeRangeEnd(rng)
        self.failUnlessIsInstance(o, QTTime)

        o = QTUnionTimeRange(rng, rng2)
        self.failUnlessIsInstance(o, QTTimeRange)

        o = QTIntersectionTimeRange(rng, rng2)
        self.failUnlessIsInstance(o, QTTimeRange)

if __name__ == "__main__":
    main()
