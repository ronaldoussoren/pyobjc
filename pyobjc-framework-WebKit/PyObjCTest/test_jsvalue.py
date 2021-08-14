import JavaScriptCore
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestJSValue(TestCase):
    @min_os_level("10.9")
    def test_classes(self):
        self.assertHasAttr(JavaScriptCore, "JSValue")

        self.assertArgIsBOOL(JavaScriptCore.JSValue.valueWithBool_inContext_, 0)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.toBool)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.deleteProperty_)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.hasProperty_)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isUndefined)

        # XXX: On macOS 12 there is a class method 'isNull' shadowing the instance method
        #      This only affects this test pattern, not normal users of the API.
        self.assertResultIsBOOL(JavaScriptCore.JSValue.pyobjc_instanceMethods.isNull)

        self.assertResultIsBOOL(JavaScriptCore.JSValue.isBoolean)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isNumber)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isString)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isObject)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isEqualToObject_)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isEqualWithTypeCoercionToObject_)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isInstanceOf_)

    @min_os_level("10.11")
    def test_classes10_11(self):
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isArray)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isDate)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            JavaScriptCore.JSValue.valueWithNewPromiseInContext_fromExecutor_, 1, b"v@@"
        )
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isSymbol)

    @min_os_level("10.9")
    def test_contants(self):
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorWritableKey, str)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorEnumerableKey, str)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorConfigurableKey, str)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorValueKey, str)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorGetKey, str)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorSetKey, str)
