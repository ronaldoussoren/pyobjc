from PyObjCTools.TestSupport import *

import JavaScriptCore
import objc

class TestJSContext (TestCase):
    @onlyOn64Bit
    @min_os_level('10.9')
    def test_classes(self):
        self.assertHasAttr(JavaScriptCore, 'JSContext')

        self.assertResultIsBlock(JavaScriptCore.JSContext.exceptionHandler, b"v@@")
        self.assertArgIsBlock(JavaScriptCore.JSContext.setExceptionHandler_, 0, b"v@@")

if __name__ == "__main__":
    main()
