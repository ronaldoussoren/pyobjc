from PyObjCTools.TestSupport import TestCase, min_os_level
import CallKit


class TestCXProviderConfiguration(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXProviderConfiguration.includesCallsInRecents)
        self.assertArgIsBOOL(
            CallKit.CXProviderConfiguration.setIncludesCallsInRecents_, 0
        )
        self.assertResultIsBOOL(CallKit.CXProviderConfiguration.supportsVideo)
        self.assertArgIsBOOL(CallKit.CXProviderConfiguration.setSupportsVideo_, 0)

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(
            CallKit.CXProviderConfiguration.supportsAudioTranslation
        )
        self.assertArgIsBOOL(
            CallKit.CXProviderConfiguration.setSupportsAudioTranslation_, 0
        )
