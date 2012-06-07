
from PyObjCTools.TestSupport import *
from QTKit import *

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

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


if __name__ == "__main__":
    main()
