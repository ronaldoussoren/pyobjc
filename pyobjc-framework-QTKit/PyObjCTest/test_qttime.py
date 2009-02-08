
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTTime (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kQTTimeIsIndefinite, 1)
        self.failUnlessIsInstance(QTZeroTime, QTTime)
        self.failUnlessIsInstance(QTIndefiniteTime, QTTime)

    def testStruct(self):
        v = QTTime()
        self.failUnless(hasattr(v, 'timeValue'))
        self.failUnless(hasattr(v, 'timeScale'))
        self.failUnless(hasattr(v, 'flags'))

        self.failIf(QTTime.__typestr__.startswith('{?'))

    def testFunctions(self):
        #v = QTMakeTimeWithTimeRecord((1, 0, 0))
        #self.failUnlessIsInstance(v, QTTime)

        v = QTMakeTimeWithTimeInterval(1500.0)
        self.failUnlessIsInstance(v, QTTime)

        #self.failUnlessResultIsBOOL(QTGetTimeRecord)
        #v, o = QTGetTimeRecord(v, None)
        #self.failUnless(v is True)

        v, o = QTGetTimeInterval(QTMakeTimeWithTimeInterval(1500.0), None)
        self.failUnless(v is True)
        self.failUnlessEqual(o, 1500.0)

        v = QTTimeCompare(QTMakeTimeWithTimeInterval(1500.0), QTMakeTimeWithTimeInterval(1500.0))
        self.failUnlessIsInstance(v, (int, long))

        v = QTMakeTimeWithTimeInterval(1500.0)
        w = QTMakeTimeWithTimeInterval(10.0)

        o = QTTimeIncrement(v, w)
        self.failUnlessIsInstance(o, QTTime)
        o = QTTimeDecrement(v, w)
        self.failUnlessIsInstance(o, QTTime)

        o = QTStringFromTime(v)
        self.failUnlessIsInstance(o, unicode)

        o = QTTimeFromString(o)
        self.failUnlessIsInstance(o, QTTime)

        self.failUnlessResultIsBOOL(QTTimeIsIndefinite)
        o = QTTimeIsIndefinite(v)
        self.failUnless(o is False)
        o = QTTimeIsIndefinite(QTIndefiniteTime)
        self.failUnless(o is True)


if __name__ == "__main__":
    main()
