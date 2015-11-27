from PyObjCTools.TestSupport import *

import JavaScriptCore
import objc

class TestJSValue (TestCase):
    @onlyOn64Bit
    @min_os_level('10.9')
    def test_classes(self):
        self.assertHasAttr(JavaScriptCore, 'JSValue')

        self.assertArgIsBOOL(JavaScriptCore.JSValue.valueWithBool_inContext_, 0)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.toBool)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.deleteProperty_)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.hasProperty_)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isUndefined)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isNull)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isBoolean)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isNumber)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isString)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isObject)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isEqualToObject_)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isEqualWithTypeCoercionToObject_)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isInstanceOf_)

    @onlyOn64Bit
    @min_os_level('10.11')
    def test_classes10_11(self):
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isArray)
        self.assertResultIsBOOL(JavaScriptCore.JSValue.isDate)


    @onlyOn64Bit
    @min_os_level('10.9')
    def test_contants(self):
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorWritableKey, unicode)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorEnumerableKey, unicode)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorConfigurableKey, unicode)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorValueKey, unicode)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorGetKey, unicode)
        self.assertIsInstance(JavaScriptCore.JSPropertyDescriptorSetKey, unicode)

if __name__ == "__main__":
    main()
