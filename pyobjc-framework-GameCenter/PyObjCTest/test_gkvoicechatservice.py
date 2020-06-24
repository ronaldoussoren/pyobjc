from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter


class TestGKVoiceChatService(TestCase):
    # NOTE: Class GKVoiceChatService is not available on OSX

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(GameCenter.GKVoiceChatServiceErrorDomain, str)
