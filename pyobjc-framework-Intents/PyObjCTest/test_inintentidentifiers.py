from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    os_level_key,
    expectedFailureIf,
)
import Intents


class TestINIntentIdentifiers(TestCase):
    @min_os_level("10.12")
    @expectedFailureIf(
        os_level_key(os_release()) < os_level_key("10.14")
    )  # Documented to be available for 10.12, but not available
    def testConstants(self):
        self.assertIsInstance(Intents.INStartAudioCallIntentIdentifier, str)
        self.assertIsInstance(Intents.INStartVideoCallIntentIdentifier, str)
        self.assertIsInstance(Intents.INSearchCallHistoryIntentIdentifier, str)
        self.assertIsInstance(Intents.INSendMessageIntentIdentifier, str)
        self.assertIsInstance(Intents.INSearchForMessagesIntentIdentifier, str)
        self.assertIsInstance(Intents.INSetMessageAttributeIntentIdentifier, str)

    @min_os_level("13.1")
    def test_constants13_1(self):
        self.assertIsInstance(Intents.INAnswerCallIntentIdentifier, str)
        self.assertIsInstance(Intents.INHangUpCallIntentIdentifier, str)
