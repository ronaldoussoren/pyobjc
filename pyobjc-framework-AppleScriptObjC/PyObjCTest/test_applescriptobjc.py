import AppleScriptObjC
import Foundation
from PyObjCTools.TestSupport import *


class TestAppleScriptObjC(TestCase):
    @min_os_level("10.6")
    def testDummy(self):
        # Nothing to test...
        self.assertHasAttr(Foundation.NSBundle, "loadAppleScriptObjectiveCScripts")


if __name__ == "__main__":
    main()
