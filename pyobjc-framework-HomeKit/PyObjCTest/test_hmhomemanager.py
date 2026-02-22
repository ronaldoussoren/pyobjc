from PyObjCTools.TestSupport import TestCase

import HomeKit  # noqa: F401


class TestHMHomeManager(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("HMHomeManagerDelegate")
