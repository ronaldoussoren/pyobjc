from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit


class TestQTTime(TestCase):
    def testConstants(self):
        self.assertEqual(QTKit.QTKit.kQTTimeIsIndefinite, 1)
        self.assertIsInstance(QTKit.QTZeroTime, QTKit.QTTime)
        self.assertIsInstance(QTKit.QTIndefiniteTime, QTKit.QTTime)

    def testStruct(self):
        v = QTKit.QTTime()
        self.assertHasAttr(v, "timeValue")
        self.assertHasAttr(v, "timeScale")
        self.assertHasAttr(v, "flags")

        self.assertFalse(QTKit.QTTime.__typestr__.startswith(b"{?"))

    def testFunctions(self):
        # v = QTKit.QTMakeTimeWithTimeRecord((1, 0, 0))
        # self.assertIsInstance(v, QTKit.QTTime)

        v = QTKit.QTMakeTimeWithTimeInterval(1500.0)
        self.assertIsInstance(v, QTKit.QTTime)

        v = QTKit.QTMakeTime(50000, 100)
        self.assertIsInstance(v, QTKit.QTTime)

        v = QTKit.QTMakeTimeScaled(v, 100)
        self.assertIsInstance(v, QTKit.QTTime)

        # self.assertResultIsBOOL(QTKit.QTGetTimeRecord)
        # v, o = QTKit.QTGetTimeRecord(v, None)
        # self.assertTrue(v is True)

        v, o = QTKit.QTGetTimeInterval(QTKit.QTMakeTimeWithTimeInterval(1500.0), None)
        self.assertTrue(v is True)
        self.assertEqual(o, 1500.0)

        v = QTKit.QTTimeCompare(
            QTKit.QTMakeTimeWithTimeInterval(1500.0),
            QTKit.QTMakeTimeWithTimeInterval(1500.0),
        )
        self.assertIsInstance(v, int)

        v = QTKit.QTMakeTimeWithTimeInterval(1500.0)
        w = QTKit.QTMakeTimeWithTimeInterval(10.0)

        o = QTKit.QTTimeIncrement(v, w)
        self.assertIsInstance(o, QTKit.QTTime)
        o = QTKit.QTTimeDecrement(v, w)
        self.assertIsInstance(o, QTKit.QTTime)

        o = QTKit.QTStringFromTime(v)
        self.assertIsInstance(o, str)

        o = QTKit.QTTimeFromString(o)
        self.assertIsInstance(o, QTKit.QTTime)

        self.assertResultIsBOOL(QTKit.QTTimeIsIndefinite)
        o = QTKit.QTTimeIsIndefinite(v)
        self.assertTrue(o is False)
        o = QTKit.QTTimeIsIndefinite(QTKit.QTIndefiniteTime)
        self.assertTrue(o is True)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        v = QTKit.QTStringFromSMPTETime((0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.assertIsInstance(v, str)
