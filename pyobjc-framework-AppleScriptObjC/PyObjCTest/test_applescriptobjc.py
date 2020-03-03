import AppleScriptObjC  # noqa: F401
import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAppleScriptObjC(TestCase):
    @min_os_level("10.6")
    def testDummy(self):
        # Nothing to test...
        self.assertHasAttr(Foundation.NSBundle, "loadAppleScriptObjectiveCScripts")
