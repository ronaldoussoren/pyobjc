import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSColorSampler(TestCase):
    @min_os_level("10.15")
    def test_methods_10_15(self):
        self.assertArgIsBlock(
            AppKit.NSColorSampler.showSamplerWithSelectionHandler_, 0, b"v@"
        )
