from PyObjCTools.TestSupport import TestCase, min_os_level

import SensitiveContentAnalysis


class TestSCSensitivityAnalysis(TestCase):
    @min_os_level("27.0")
    def test_constants(self):
        self.assertIsTypedEnum(SensitiveContentAnalysis.SCSensitiveContentType, str)
        self.assertIsInstance(
            SensitiveContentAnalysis.SCSensitiveContentTypeSexuallyExplicit, str
        )
        self.assertIsInstance(
            SensitiveContentAnalysis.SCSensitiveContentTypeGoreOrViolence, str
        )

    def test_methods(self):
        self.assertResultIsBOOL(
            SensitiveContentAnalysis.SCSensitivityAnalysis.isSensitive
        )
