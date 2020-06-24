import JavaScriptCore
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestJSVirtualMachine(TestCase):
    @min_os_level("10.9")
    def test_classes(self):
        self.assertHasAttr(JavaScriptCore, "JSVirtualMachine")
