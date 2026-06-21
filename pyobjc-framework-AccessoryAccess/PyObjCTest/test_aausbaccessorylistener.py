from PyObjCTools.TestSupport import TestCase

import AccessoryAccess


class TestAAUSBAccessoryListener(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("AAUSBAccessoryListener", AccessoryAccess)
