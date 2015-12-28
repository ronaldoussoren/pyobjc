from PyObjCTools.TestSupport import *

from ImageCaptureCore import *

class TestICCameraDevice (TestCase):

    def testMethods(self):
        self.assertResultIsBOOL(ICCameraItem.isLocked)
        self.assertResultIsBOOL(ICCameraItem.isInTemporaryStore)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(ICCameraItem.isRaw)
        self.assertResultIsBOOL(ICCameraItem.wasAddedAfterContentCatalogCompleted)

if __name__ == "__main__":
    main()
