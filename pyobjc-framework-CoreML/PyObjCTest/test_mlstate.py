from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLState(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsBlock(
            CoreML.MLState.getMultiArrayForStateNamed_handler_, 1, b"v@"
        )
