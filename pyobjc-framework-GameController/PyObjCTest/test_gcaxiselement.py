from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
)
import objc
import GameController  # noqa: F401


class TestGCAxisElement(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        objc.protocolNamed("GCAxisElement")
