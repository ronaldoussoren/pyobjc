
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTTime (TestCase):
    def testConstants(self):
        self.assertEqual(kQTTimeIsIndefinite, 1)
        self.assertIsInstance(QTZeroTime, QTTime)
        self.assertIsInstance(QTIndefiniteTime, QTTime)

    def testStruct(self):
        v = QTTime()
        self.assertHasAttr(v, 'timeValue')
        self.assertHasAttr(v, 'timeScale')
        self.assertHasAttr(v, 'flags')

        self.assertFalse(QTTime.__typestr__.startswith(b'{?'))

    def testFunctions(self):
        #v = QTMakeTimeWithTimeRecord((1, 0, 0))
        #self.assertIsInstance(v, QTTime)

        v = QTMakeTimeWithTimeInterval(1500.0)
        self.assertIsInstance(v, QTTime)

        v = QTMakeTime(50000, 100)
        self.assertIsInstance(v, QTTime)

        v = QTMakeTimeScaled(v, 100)
        self.assertIsInstance(v, QTTime)

        #self.assertResultIsBOOL(QTGetTimeRecord)
        #v, o = QTGetTimeRecord(v, None)
        #self.assertTrue(v is True)

        v, o = QTGetTimeInterval(QTMakeTimeWithTimeInterval(1500.0), None)
        self.assertTrue(v is True)
        self.assertEqual(o, 1500.0)

        v = QTTimeCompare(QTMakeTimeWithTimeInterval(1500.0), QTMakeTimeWithTimeInterval(1500.0))
        self.assertIsInstance(v, (int, long))

        v = QTMakeTimeWithTimeInterval(1500.0)
        w = QTMakeTimeWithTimeInterval(10.0)

        o = QTTimeIncrement(v, w)
        self.assertIsInstance(o, QTTime)
        o = QTTimeDecrement(v, w)
        self.assertIsInstance(o, QTTime)

        o = QTStringFromTime(v)
        self.assertIsInstance(o, unicode)

        o = QTTimeFromString(o)
        self.assertIsInstance(o, QTTime)

        self.assertResultIsBOOL(QTTimeIsIndefinite)
        o = QTTimeIsIndefinite(v)
        self.assertTrue(o is False)
        o = QTTimeIsIndefinite(QTIndefiniteTime)
        self.assertTrue(o is True)

    @min_os_level('10.5')
    def testFunctions10_5(self):
        v = QTStringFromSMPTETime((0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.assertIsInstance(v, unicode)



if __name__ == "__main__":
    main()
