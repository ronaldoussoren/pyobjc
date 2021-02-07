from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos


class TestPHProject(TestCase):
    @min_os_level("10.14")
    def test_methods(self):
        self.assertResultIsBOOL(Photos.PHProject.hasProjectPreview)
