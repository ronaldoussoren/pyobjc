import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestBELayerHierarchyHostingTransactionCoordinator(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertArgIsOut(
            BrowserEngineKit.BELayerHierarchyHostingTransactionCoordinator.coordinatorWithPort_data_error_,
            2,
        )
        self.assertArgIsBlock(
            BrowserEngineKit.BELayerHierarchyHostingTransactionCoordinator.encodeWithBlock_,
            0,
            b"vi@",
        )
