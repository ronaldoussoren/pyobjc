from PyObjCTools.TestSupport import *

from ImageCaptureCore import *

class TestICCameraDevice (TestCase):

    def testMethods(self):
        self.assertResultIsBOOL(ICCameraItem.isLocked)
        self.assertResultIsBOOL(ICCameraItem.isRaw)
        self.assertResultIsBOOL(ICCameraItem.isInTemporaryStore)
        self.assertResultIsBOOL(ICCameraItem.wasAddedAfterContentCatalogCompleted)

if __name__ == "__main__":
    main()
