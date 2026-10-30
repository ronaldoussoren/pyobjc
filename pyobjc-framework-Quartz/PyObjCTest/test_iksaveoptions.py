from PyObjCTools.TestSupport import TestCase
import Quartz


class TestIKSaveOptionsHelper(Quartz.NSObject):
    def saveOptions_shouldShowUTType_(self, o, t):
        return 1


class TestIKSaveOptions(TestCase):
    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestIKSaveOptionsHelper.saveOptions_shouldShowUTType_)
