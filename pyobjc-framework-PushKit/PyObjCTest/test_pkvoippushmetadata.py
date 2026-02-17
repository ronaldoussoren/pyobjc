from PyObjCTools.TestSupport import TestCase, min_os_level

import PushKit


class TestPKVoIPPushMetadata(TestCase):
    @min_os_level("26.4")
    def test_methods(self):
        self.assertResultIsBOOL(PushKit.PKVoIPPushMetadata.mustReport)
