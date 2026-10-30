import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSCachedImageRep(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(
            AppKit.NSCachedImageRep.initWithSize_depth_separate_alpha_, 2
        )
        self.assertArgIsBOOL(
            AppKit.NSCachedImageRep.initWithSize_depth_separate_alpha_, 3
        )
