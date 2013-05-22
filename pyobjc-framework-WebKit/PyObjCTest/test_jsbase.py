from PyObjCTools.TestSupport import *

import JavaScriptCore
import objc

class TestJSBase (TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(JavaScriptCore.JSContextGroupRef)
        self.assertIsOpaquePointer(JavaScriptCore.JSContextRef)
        self.assertIsOpaquePointer(JavaScriptCore.JSStringRef)
        self.assertIsOpaquePointer(JavaScriptCore.JSPropertyNameArrayRef)
        self.assertIsOpaquePointer(JavaScriptCore.JSPropertyNameAccumulatorRef)
        self.assertIsOpaquePointer(JavaScriptCore.JSValueRef)

        self.assertIs(JavasScriptCore.JSObjectRef, JavaScriptCore.JSValueRef)
        self.assertIs(JavasScriptCore.JSGlobalContextRef, JavaScriptCore.JSContextRef)

    def test_functions(self):
        self.assertResultHasType(JavaScriptCore.JSEvaluateScript, JavaScriptCore.JSValueRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSEvaluateScript, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSEvaluateScript, 1, JavaScriptCore.JSStringRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSEvaluateScript, 2, JavaScriptCore.JSValueRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSEvaluateScript, 3, JavaScriptCore.JSStringRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSEvaluateScript, 4, objc._C_INT)
        self.assertArgHasType(JavaScriptCore.JSEvaluateScript, 5, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(objc._C_BOOL, JavaScriptCore.JSCheckScriptSyntax)
        self.assertArgIsOut(JavaScriptCore.JSCheckScriptSyntax, 4)

        self.assertArgHasType(JavaScriptCore.JSGarbageCollect, 0, JavaScriptCore.JSContextRef.__typestr__)

if __name__ == "__main__":
    main()
