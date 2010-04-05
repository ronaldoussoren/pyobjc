from Quartz import *
from PyObjCTools.TestSupport import *

class TestIKSaveOptionsHelper (NSObject):
    def saveOptions_shouldShowUTType_(self, o, t): return 1

class TestIKSaveOptions (TestCase):

    @min_os_level('10.6')
    def testProtocol10_6(self):
        self.assertResultIsBOOL(TestIKSaveOptionsHelper.saveOptions_shouldShowUTType_)


if __name__ == "__main__":
    main()
