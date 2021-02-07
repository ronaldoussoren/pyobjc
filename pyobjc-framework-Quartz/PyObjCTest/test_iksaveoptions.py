from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz  # noqa: F401


class TestIKSaveOptionsHelper(Quartz.NSObject):
    def saveOptions_shouldShowUTType_(self, o, t):
        return 1


class TestIKSaveOptions(TestCase):
    @min_os_level("10.6")
    def testProtocol10_6(self):
        self.assertResultIsBOOL(TestIKSaveOptionsHelper.saveOptions_shouldShowUTType_)
