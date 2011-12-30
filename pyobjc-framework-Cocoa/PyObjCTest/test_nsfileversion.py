from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSFileVersion (TestCase):
    @min_os_level('10.7')
    def testContants10_7(self):
        self.assertEqual(NSFileVersionAddingByMoving, 1<<0)
        self.assertEqual(NSFileVersionReplacingByMoving, 1<<0)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsOut(NSFileVersion.addVersionOfItemAtURL_withContentsOfURL_options_error_, 3)
        self.assertArgIsOut(NSFileVersion.replaceItemAtURL_options_error_, 2)
        self.assertArgIsOut(NSFileVersion.removeAndReturnError_, 0)
        self.assertResultIsBOOL(NSFileVersion.removeAndReturnError_)

        self.assertArgIsOut(NSFileVersion.removeOtherVersionsOfItemAtURL_error_, 1)
        self.assertResultIsBOOL(NSFileVersion.removeOtherVersionsOfItemAtURL_error_)

        self.assertResultIsBOOL(NSFileVersion.isConflict)

        self.assertArgIsBOOL(NSFileVersion.setResolved_, 0)
        self.assertResultIsBOOL(NSFileVersion.isResolved)
        self.assertArgIsBOOL(NSFileVersion.setDiscardable_, 0)
        self.assertResultIsBOOL(NSFileVersion.isDiscardable)

if __name__ == "__main__":
    main()
