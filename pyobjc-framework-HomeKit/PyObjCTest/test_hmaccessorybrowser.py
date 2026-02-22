from PyObjCTools.TestSupport import TestCase

import HomeKit  # noqa: F401


class TestHMAccessoryBrowser(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("HMAccessoryBrowserDelegate")
