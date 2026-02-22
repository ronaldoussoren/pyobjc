from PyObjCTools.TestSupport import TestCase

import HomeKit  # noqa: F401


class TestHMAccessory(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("HMAccessoryDelegate")
