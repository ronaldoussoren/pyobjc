from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos


class TestPHChange(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(Photos.PHObjectChangeDetails.assetContentChanged)
        self.assertResultIsBOOL(Photos.PHObjectChangeDetails.objectWasDeleted)

        self.assertResultIsBOOL(Photos.PHFetchResultChangeDetails.hasIncrementalChanges)
        self.assertResultIsBOOL(Photos.PHFetchResultChangeDetails.hasMoves)
