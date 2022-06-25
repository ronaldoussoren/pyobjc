from PyObjCTools.TestSupport import TestCase, min_sdk_level
import CoreML  # noqa: F401


class TestMLDictionaryFeatureProvider(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("MLFeatureProvider")
