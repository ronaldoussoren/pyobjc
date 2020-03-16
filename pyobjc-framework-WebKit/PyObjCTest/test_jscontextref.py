import JavaScriptCore
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestJSContextRef(TestCase):
    def test_functions(self):
        self.assertResultHasType(
            JavaScriptCore.JSContextGroupCreate,
            JavaScriptCore.JSContextGroupRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSContextGroupRetain,
            JavaScriptCore.JSContextGroupRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSContextGroupRetain,
            0,
            JavaScriptCore.JSContextGroupRef.__typestr__,
        )

        self.assertArgHasType(
            JavaScriptCore.JSContextGroupRelease,
            0,
            JavaScriptCore.JSContextGroupRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSGlobalContextCreate,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSGlobalContextCreate,
            0,
            JavaScriptCore.JSClassRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSGlobalContextCreateInGroup,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSGlobalContextCreateInGroup,
            0,
            JavaScriptCore.JSContextGroupRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSGlobalContextCreateInGroup,
            1,
            JavaScriptCore.JSClassRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSGlobalContextRetain,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSGlobalContextRetain,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )

        self.assertArgHasType(
            JavaScriptCore.JSGlobalContextRelease,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSContextGetGlobalObject,
            JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSContextGetGlobalObject,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSContextGetGroup,
            JavaScriptCore.JSContextGroupRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSContextGetGroup, 0, JavaScriptCore.JSContextRef.__typestr__
        )

    @min_os_level("10.7")
    def test_functions10_7(self):
        self.assertResultHasType(
            JavaScriptCore.JSContextGetGlobalContext,
            JavaScriptCore.JSGlobalContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSContextGetGlobalContext,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )

    @min_os_level("10.10")
    def test_functions10_10(self):
        self.assertResultHasType(
            JavaScriptCore.JSGlobalContextCopyName,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSGlobalContextCopyName,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )

        self.assertResultHasType(JavaScriptCore.JSGlobalContextSetName, objc._C_VOID)
        self.assertArgHasType(
            JavaScriptCore.JSGlobalContextSetName,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSGlobalContextSetName,
            1,
            JavaScriptCore.JSStringRef.__typestr__,
        )
