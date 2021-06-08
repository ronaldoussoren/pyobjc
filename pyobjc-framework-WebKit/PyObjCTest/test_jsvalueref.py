import JavaScriptCore
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestJSValueRef(TestCase):
    def test_constants(self):
        self.assertEqual(JavaScriptCore.kJSTypeUndefined, 0)
        self.assertEqual(JavaScriptCore.kJSTypeNull, 1)
        self.assertEqual(JavaScriptCore.kJSTypeBoolean, 2)
        self.assertEqual(JavaScriptCore.kJSTypeNumber, 3)
        self.assertEqual(JavaScriptCore.kJSTypeString, 4)
        self.assertEqual(JavaScriptCore.kJSTypeObject, 5)
        self.assertEqual(JavaScriptCore.kJSTypeSymbol, 6)

        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeInt8Array, 0)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeInt16Array, 1)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeInt32Array, 2)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeUint8Array, 3)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeUint8ClampedArray, 4)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeUint16Array, 5)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeUint32Array, 6)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeFloat32Array, 7)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeFloat64Array, 8)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeArrayBuffer, 9)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeNone, 10)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeBigInt64Array, 11)
        self.assertEqual(JavaScriptCore.kJSTypedArrayTypeBigUint64Array, 12)

    def test_functions(self):
        self.assertArgHasType(
            JavaScriptCore.JSValueGetType, 0, JavaScriptCore.JSContextRef.__typestr__
        )

        self.assertResultHasType(JavaScriptCore.JSValueIsUndefined, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsNull, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsBoolean, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsNumber, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsString, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsObject, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsObjectOfClass, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsEqual, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsStrictEqual, objc._C_BOOL)
        self.assertResultHasType(
            JavaScriptCore.JSValueIsInstanceOfConstructor, objc._C_BOOL
        )

        self.assertResultHasType(
            JavaScriptCore.JSValueMakeUndefined, JavaScriptCore.JSValueRef.__typestr__
        )
        self.assertResultHasType(
            JavaScriptCore.JSValueMakeNull, JavaScriptCore.JSValueRef.__typestr__
        )
        self.assertResultHasType(
            JavaScriptCore.JSValueMakeBoolean, JavaScriptCore.JSValueRef.__typestr__
        )
        self.assertResultHasType(
            JavaScriptCore.JSValueMakeNumber, JavaScriptCore.JSValueRef.__typestr__
        )
        self.assertResultHasType(
            JavaScriptCore.JSValueMakeString, JavaScriptCore.JSValueRef.__typestr__
        )
        self.assertResultHasType(
            JavaScriptCore.JSValueMakeFromJSONString,
            JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertResultHasType(
            JavaScriptCore.JSValueCreateJSONString,
            JavaScriptCore.JSStringRef.__typestr__,
        )

        self.assertResultHasType(JavaScriptCore.JSValueToBoolean, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueToNumber, objc._C_DBL)
        self.assertResultHasType(
            JavaScriptCore.JSValueToStringCopy, JavaScriptCore.JSStringRef.__typestr__
        )
        self.assertResultHasType(
            JavaScriptCore.JSValueToObject, JavaScriptCore.JSObjectRef.__typestr__
        )

        self.assertArgHasType(
            JavaScriptCore.JSValueProtect, 0, JavaScriptCore.JSContextRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSValueUnprotect, 0, JavaScriptCore.JSContextRef.__typestr__
        )

    @min_os_level("10.11")
    def testFunctions10_11(self):
        self.assertResultHasType(JavaScriptCore.JSValueIsArray, objc._C_BOOL)
        self.assertResultHasType(JavaScriptCore.JSValueIsDate, objc._C_BOOL)

    @min_os_level("10.12")
    def testFunctions10_12(self):
        self.assertResultHasType(JavaScriptCore.JSValueGetTypedArrayType, objc._C_UINT)
        self.assertArgIsOut(JavaScriptCore.JSValueGetTypedArrayType, 2)

    @min_os_level("10.14.4")
    def testFunctions10_14_4(self):
        self.assertResultHasType(
            JavaScriptCore.JSValueMakeSymbol, JavaScriptCore.JSValueRef.__typestr__
        )

    @min_os_level("10.15")
    def testFunctions10_15(self):
        JavaScriptCore.JSValueIsSymbol
        JavaScriptCore.JSValueMakeSymbol
