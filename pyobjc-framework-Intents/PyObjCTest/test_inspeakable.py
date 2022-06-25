from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Intents  # noqa: F401


class TestINSpeakable(TestCase):
    @min_sdk_level("10.12")
    def testProtocols(self):
        self.assertProtocolExists("INSpeakable")
