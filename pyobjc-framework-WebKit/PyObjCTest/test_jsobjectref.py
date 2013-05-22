from PyObjCTools.TestSupport import *

import JavaScriptCore
import objc


class TestJSObjectRef (TestCase):
    def test_values(self):
        self.assertEqual(JavaScriptCore.kJSPropertyAttributeNone, 0)
        self.assertEqual(JavaScriptCore.kJSPropertyAttributeReadOnly, 1<<1)
        self.assertEqual(JavaScriptCore.kJSPropertyAttributeDontEnum, 1<<2)
        self.assertEqual(JavaScriptCore.kJSPropertyAttributeDontDelete, 1<<3)

        self.assertEqual(JavaScriptCore.kJSClassAttributeNone, 0)
        self.assertEqual(JavaScriptCore.kJSClassAttributeNoAutomaticPrototype, 1<<1)

    def test_functions(self):
        self.fail("Need to think about these wrappers....")


        definition = JavaScriptCore.kJSClassDefinitionEmpty.copy()
        cls = JavaScriptCore.JSClassCreate(definition)
        self.assertIsInstance(cls, JavaScriptCore.JSClassRef)

        self.assertResultHasType(JavaScriptCore.JSClassRetain, JavaScriptCore.JSClassRef)
        self.assertArgHasType(JavaScriptCore.JSClassRetain, 0, JavaScriptCore.JSClassRef)

        self.assertArgHasType(JavaScriptCore.JSClassRelease, 0, JavaScriptCore.JSClassRef)

        # JSObjectMake
        # JSObjectMakeFunctionWithCallback
        # JSObjectMakeConstructor
        # JSObjectMakeArray
        # JSObjectMakeDate
        # JSObjectMakeError
        # JSObjectMakeRegExp
        # JSObjectMakeFunction
        # JSObjectGetPrototype
        # JSObjectSetPrototype
        # JSObjectHasProperty
        # JSObjectGetProperty
        # JSObjectSetProperty
        # JSObjectDeleteProperty
        # JSObjectGetPropertyAtIndex
        # JSObjectSetPropertyAtIndex
        # JSObjectGetPrivate
        # JSObjectSetPrivate
        # JSObjectIsFunction
        # JSObjectCallAsFunction
        # JSObjectIsConstructor
        # JSObjectCallAsConstructor
        # JSObjectCopyPropertyNames
        # JSPropertyNameArrayRetain
        # JSPropertyNameArrayRelease
        # JSPropertyNameArrayGetCount
        # JSPropertyNameArrayGetNameAtIndex
        # JSPropertyNameAccumulatorAddName

if __name__ == "__main__":
    main()
