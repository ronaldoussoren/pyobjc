from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTUtilities(TestCase):
    def testFunctions(self):
        v = QTKit.QTStringForOSType(15490)
        self.assertIsInstance(v, str)

        w = QTKit.QTOSTypeForString(v)
        self.assertIsInstance(w, int)
        self.assertEqual(w, 15490)
