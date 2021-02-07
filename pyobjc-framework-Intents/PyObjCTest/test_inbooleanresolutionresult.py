from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINBooleanResolutionResult(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBOOL(
            Intents.INBooleanResolutionResult.successWithResolvedValue_, 0
        )
