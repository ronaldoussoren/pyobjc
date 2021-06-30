from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINBooleanResolutionResult(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsBOOL(
            Intents.INBooleanResolutionResult.successWithResolvedValue_, 0
        )
