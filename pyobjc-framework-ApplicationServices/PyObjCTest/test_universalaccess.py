import HIServices
from PyObjCTools.TestSupport import TestCase


class TestUniversalAccess(TestCase):
    def test_constants(self):
        self.assertEqual(HIServices.kUAZoomFocusTypeOther, 0)
        self.assertEqual(HIServices.kUAZoomFocusTypeInsertionPoint, 1)

    def test_functions(self):
        self.assertResultIsBOOL(HIServices.UAZoomEnabled)

        self.assertArgIsIn(HIServices.UAZoomChangeFocus, 0)
        self.assertArgIsIn(HIServices.UAZoomChangeFocus, 1)
