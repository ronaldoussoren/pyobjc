from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINParameter(TestCase):
    @min_os_level("10.14")
    def test_methods(self):
        self.assertResultIsBOOL(Intents.INParameter.isEqualToParameter_)
