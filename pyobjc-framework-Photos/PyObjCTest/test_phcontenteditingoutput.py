from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import Photos


class TestPHContentEditingOutput(TestCase):
    @min_os_level("10.11")
    def testClasses(self):
        self.assertIsInstance(Photos.PHContentEditingOutput, objc.objc_class)

        @min_os_level("14.0")
        def test_methods(self):
            self.assertArgIsOut(
                Photos.PHContentEditingOutput.renderedContentURLForType_error_, 1
            )
