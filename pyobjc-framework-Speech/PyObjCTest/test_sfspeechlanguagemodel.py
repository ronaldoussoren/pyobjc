import Speech
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSFSpeechLanguageModel(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Speech.SFSpeechLanguageModel.prepareCustomLanguageModelForUrl_clientIdentifier_configuration_completion_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            Speech.SFSpeechLanguageModel.prepareCustomLanguageModelForUrl_clientIdentifier_configuration_ignoresCache_completion_,
            4,
            b"v@",
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertArgIsBlock(
            Speech.SFSpeechLanguageModel.prepareCustomLanguageModelForUrl_configuration_completion_,
            2,
            b"v@",
        )

        self.assertArgIsBOOL(
            Speech.SFSpeechLanguageModel.prepareCustomLanguageModelForUrl_configuration_ignoresCache_completion_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            Speech.SFSpeechLanguageModel.prepareCustomLanguageModelForUrl_configuration_ignoresCache_completion_,
            4,
            b"v@",
        )
