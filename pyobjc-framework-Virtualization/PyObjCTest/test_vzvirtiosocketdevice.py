from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZVirtioSocketDevice(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            Virtualization.VZVirtioSocketDevice.connectToPort_completionHandler_,
            1,
            b"v@@",
        )
