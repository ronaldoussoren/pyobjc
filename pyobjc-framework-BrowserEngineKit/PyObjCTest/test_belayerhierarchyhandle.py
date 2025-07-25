import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestBELayerHierarchyHandle(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertArgIsOut(
            BrowserEngineKit.BELayerHierarchyHandle.handleWithPort_data_error_, 2
        )
        self.assertArgIsBlock(
            BrowserEngineKit.BELayerHierarchyHandle.encodeWithBlock_, 0, b"vi@"
        )
