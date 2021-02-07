from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos


class TestPHCloudIdentifier(TestCase):
    @min_os_level("10.13")
    def testConstants(self):
        self.assertIsInstance(Photos.PHLocalIdentifierNotFound, str)
