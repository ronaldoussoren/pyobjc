from PyObjCTools.TestSupport import *

import JavaScriptCore

class TestJSValueRef (TestCase):
    def test_constants(self):
        self.assertEqual(JavaScriptCore.kJSTypeUndefined, 0)
        self.assertEqual(JavaScriptCore.kJSTypeNull, 1)
        self.assertEqual(JavaScriptCore.kJSTypeBoolean, 2)
        self.assertEqual(JavaScriptCore.kJSTypeNumber, 3)
        self.assertEqual(JavaScriptCore.kJSTypeString, 4)
        self.assertEqual(JavaScriptCore.kJSTypeObject, 5)

    def test_functions(self):
        self.assertArgHasType(JavaScriptCore.JSValueGetType, 0, JavaScriptCore.JSContextRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSValueIsUndefined, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsNull, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsBoolean, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsNumber, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsString, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsObject, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsObjectOfClass, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsEqual, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsStrictEqual, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsInstanceOfConstructor, objc._C_BOOL)

        self.assertResultHasType(JavaScriptCore.JSValueMakeUndefined, JavaScriptCore.JSValueRef.__typestr__)
        self.assertResultHasType(JavaScriptCore.JSValueMakeNull, JavaScriptCore.JSValueRef.__typestr__)
        self.assertResultHasType(JavaScriptCore.JSValueMakeBoolean, JavaScriptCore.JSValueRef.__typestr__)
        self.assertResultHasType(JavaScriptCore.JSValueMakeNumber, JavaScriptCore.JSValueRef.__typestr__)
        self.assertResultHasType(JavaScriptCore.JSValueMakeString, JavaScriptCore.JSValueRef.__typestr__)
        self.assertResultHasType(JavaScriptCore.JSValueMakeFromJSONString, JavaScriptCore.JSValueRef.__typestr__)
        self.assertResultHasType(JavaScriptCore.JSValueCreateJSONString, JavaScriptCore.JSStringRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSValueToBoolean, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueToNumber, objc._C_DBL)
        self.assertResultHasType(JavaScriptCore.JSValueToStringCopy, JavaScriptCore.JSStringRef.__typestr__)
        self.assertResultHasType(JavaScriptCore.JSValueToObject, JavaScriptCore.JSObjectRef.__typestr__)

        self.assertArgHasType(JavaScriptCore.JSValueProtect, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSValueUnprotect, 0, JavaScriptCore.JSContextRef.__typestr__)

if __name__ == "__main__":
    main()
