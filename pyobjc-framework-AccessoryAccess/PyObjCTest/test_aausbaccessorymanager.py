from PyObjCTools.TestSupport import TestCase

import AccessoryAccess


class TestAAUSBAccessoryManager(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            AccessoryAccess.AAUSBAccessoryManager.registerListener_withMatchingCriteria_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            AccessoryAccess.AAUSBAccessoryManager.unregisterListener_completionHandler_,
            1,
            b"v@",
        )
