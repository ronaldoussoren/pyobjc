from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXProviderConfiguration(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXProviderConfiguration.includesCallsInRecents)
        self.assertArgIsBOOL(
            CallKit.CXProviderConfiguration.setIncludesCallsInRecents_, 0
        )
        self.assertResultIsBOOL(CallKit.CXProviderConfiguration.supportsVideo)
        self.assertArgIsBOOL(CallKit.CXProviderConfiguration.setSupportsVideo_, 0)
