import JavaScriptCore
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestJSContext(TestCase):
    def test_methods(self):
        self.assertResultIsBlock(JavaScriptCore.JSContext.exceptionHandler, b"v@@")
        self.assertArgIsBlock(JavaScriptCore.JSContext.setExceptionHandler_, 0, b"v@@")

    @min_os_level("13.3")
    def test_methods13_3(self):
        self.assertResultIsBOOL(JavaScriptCore.JSContext.isInspectable)
        self.assertArgIsBOOL(JavaScriptCore.JSContext.setInspectable_, 0)
