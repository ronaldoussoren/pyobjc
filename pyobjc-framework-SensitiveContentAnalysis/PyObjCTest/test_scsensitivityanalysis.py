from PyObjCTools.TestSupport import TestCase

import SensitiveContentAnalysis


class TestSCSensitivityAnalysis(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            SensitiveContentAnalysis.SCSensitivityAnalysis.isSensitive
        )
