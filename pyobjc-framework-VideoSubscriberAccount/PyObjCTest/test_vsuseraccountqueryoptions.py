from PyObjCTools.TestSupport import TestCase

import VideoSubscriberAccount


class TestVSUserAccountQueryOptions(TestCase):
    def test_constants(self):
        self.assertEqual(VideoSubscriberAccount.VSUserAccountQueryOptionNone, 0)
        self.assertEqual(VideoSubscriberAccount.VSUserAccountQueryOptionAllDevices, 1)
