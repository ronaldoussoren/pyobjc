import AppKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSPreviewRepresentingActivityItem(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        objc.protocolNamed("NSPreviewRepresentableActivityItem")
