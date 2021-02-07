from PyObjCTools.TestSupport import TestCase, min_os_level

import PushKit


class TestPKPushCredentials(TestCase):
    @min_os_level("10.15")
    def test_classes(self):
        PushKit.PKPushCredentials
