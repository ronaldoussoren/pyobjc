from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKVoiceChatService(TestCase):
    def test_constants(self):
        self.assertIsInstance(GameCenter.GKVoiceChatServiceErrorDomain, str)
