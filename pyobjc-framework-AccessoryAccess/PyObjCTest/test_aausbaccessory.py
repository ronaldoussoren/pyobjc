from PyObjCTools.TestSupport import TestCase

import AccessoryAccess


class TestAAUSBAccessory(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            AccessoryAccess.AAUSBAccessory.openWithServiceQueue_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AccessoryAccess.AAUSBAccessory.closeWithCompletionHandler_, 0, b"v@"
        )
