import JavaScriptCore
from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit


class TestJSVirtualMachine(TestCase):
    @onlyOn64Bit
    @min_os_level("10.9")
    def test_classes(self):
        self.assertHasAttr(JavaScriptCore, "JSVirtualMachine")
