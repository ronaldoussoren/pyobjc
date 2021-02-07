from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLFeatureDescription(TestCase):
    @min_os_level("10.13")
    def testConstants(self):
        self.assertIsInstance(CoreML.MLModelDescriptionKey, str)
        self.assertIsInstance(CoreML.MLModelVersionStringKey, str)
        self.assertIsInstance(CoreML.MLModelAuthorKey, str)
        self.assertIsInstance(CoreML.MLModelLicenseKey, str)
        self.assertIsInstance(CoreML.MLModelCreatorDefinedKey, str)
