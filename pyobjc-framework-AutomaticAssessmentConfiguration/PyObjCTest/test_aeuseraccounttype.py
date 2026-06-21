import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEUserAccountType(TestCase):
    @min_os_level("27.0")
    def test_constants(self):
        self.assertIsEnumType(AutomaticAssessmentConfiguration.AEUserAccountType)
        self.assertEqual(AutomaticAssessmentConfiguration.AEUserAccountTypeAny, 0)
        self.assertEqual(AutomaticAssessmentConfiguration.AEUserAccountTypeStandard, 1)
        self.assertEqual(AutomaticAssessmentConfiguration.AEUserAccountTypeGuest, 2)
