from PyObjCTools.TestSupport import *

import JavaScriptCore
import objc

class TestJSContextRef (TestCase):
    def test_functions(self):
        self.assertResultHasType(JavaScriptCore.JSContextGroupCreate, JavaScriptCore.JSContextGroupRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSContextGroupRetain, JavaScriptCore.JSContextGroupRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSContextGroupRetain, 0, JavaScriptCore.JSContextGroupRef.__typestr__)

        self.assertArgHasType(JavaScriptCore.JSContextGroupRelease, 0, JavaScriptCore.JSContextGroupRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSGlobalContextCreate, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSGlobalContextCreate, 0, JavaScriptCore.JSClassRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSGlobalContextCreateInGroup, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSGlobalContextCreateInGroup, 0, JavaScriptCore.JSContextGroupRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSGlobalContextCreateInGroup, 1, JavaScriptCore.JSClassRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSGlobalContextRetain, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSGlobalContextRetain, 0, JavaScriptCore.JSContextRef.__typestr__)

        self.assertArgHasType(JavaScriptCore.JSGlobalContextRelease, 0, JavaScriptCore.JSContextRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSContextGetGlobalObject, JavaScriptCore.JSValueRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSContextGetGlobalObject, 0, JavaScriptCore.JSContextRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSContextGetGroup, JavaScriptCore.JSContextGroupRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSContextGetGroup, 0, JavaScriptCore.JSContextRef.__typestr__)


if __name__ == "__main__":
    main()
