from PyObjCTools.TestSupport import TestCase
import XgridFoundation


class TestXGController(TestCase):
    def testConstants(self):
        self.assertIsInstance(XgridFoundation.XGControllerWillDeallocNotification, str)
