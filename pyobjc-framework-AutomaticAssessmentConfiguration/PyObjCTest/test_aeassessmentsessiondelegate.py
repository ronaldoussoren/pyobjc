import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAEAssessmentSessionDelegate(TestCase):
    @min_sdk_level("10.15.4")
    def test_protocols(self):
        self.assertProtocolExists(
            "AEAssessmentSessionDelegate", AutomaticAssessmentConfiguration
        )
