import JavaScriptCore
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestJSObjectRef(TestCase):
    def test_values(self):
        self.assertEqual(JavaScriptCore.kJSPropertyAttributeNone, 0)
        self.assertEqual(JavaScriptCore.kJSPropertyAttributeReadOnly, 1 << 1)
        self.assertEqual(JavaScriptCore.kJSPropertyAttributeDontEnum, 1 << 2)
        self.assertEqual(JavaScriptCore.kJSPropertyAttributeDontDelete, 1 << 3)

        self.assertEqual(JavaScriptCore.kJSClassAttributeNone, 0)
        self.assertEqual(JavaScriptCore.kJSClassAttributeNoAutomaticPrototype, 1 << 1)

    def test_simple_functions(self):
        self.assertResultHasType(
            JavaScriptCore.JSClassRetain, JavaScriptCore.JSClassRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSClassRetain, 0, JavaScriptCore.JSClassRef.__typestr__
        )

        self.assertArgHasType(
            JavaScriptCore.JSClassRelease, 0, JavaScriptCore.JSClassRef.__typestr__
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectMake, JavaScriptCore.JSObjectRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMake, 0, JavaScriptCore.JSContextRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMake, 1, JavaScriptCore.JSClassRef.__typestr__
        )
        self.assertArgHasType(JavaScriptCore.JSObjectMake, 2, objc._C_PTR + objc._C_VOID)

        self.assertResultHasType(
            JavaScriptCore.JSObjectMakeArray, JavaScriptCore.JSObjectRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeArray, 0, JavaScriptCore.JSContextRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeArray,
            2,
            b"n^" + JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgSizeInArg(JavaScriptCore.JSObjectMakeArray, 2, 1)
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeArray,
            3,
            b"o^" + JavaScriptCore.JSValueRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectMakeDate, JavaScriptCore.JSObjectRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeDate, 0, JavaScriptCore.JSContextRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeDate,
            2,
            b"n^" + JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgSizeInArg(JavaScriptCore.JSObjectMakeDate, 2, 1)
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeDate,
            3,
            b"o^" + JavaScriptCore.JSValueRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectMakeError, JavaScriptCore.JSObjectRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeError, 0, JavaScriptCore.JSContextRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeError,
            2,
            b"n^" + JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgSizeInArg(JavaScriptCore.JSObjectMakeError, 2, 1)
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeError,
            3,
            b"o^" + JavaScriptCore.JSValueRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectMakeRegExp, JavaScriptCore.JSObjectRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeRegExp,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeRegExp,
            2,
            b"n^" + JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgSizeInArg(JavaScriptCore.JSObjectMakeRegExp, 2, 1)
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeRegExp,
            3,
            b"o^" + JavaScriptCore.JSValueRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectMakeFunction, JavaScriptCore.JSObjectRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeFunction,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeFunction,
            1,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeFunction,
            3,
            b"n^" + JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgSizeInArg(JavaScriptCore.JSObjectMakeFunction, 3, 2)
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeFunction,
            4,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeFunction,
            5,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeFunction,
            7,
            b"o^" + JavaScriptCore.JSValueRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectGetPrototype, JavaScriptCore.JSValueRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetPrototype,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetPrototype,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )

        self.assertArgHasType(
            JavaScriptCore.JSObjectSetPrototype,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetPrototype,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetPrototype,
            2,
            JavaScriptCore.JSValueRef.__typestr__,
        )

        self.assertResultHasType(JavaScriptCore.JSObjectHasProperty, objc._C_BOOL)
        self.assertArgHasType(
            JavaScriptCore.JSObjectHasProperty,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectHasProperty,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectHasProperty,
            2,
            JavaScriptCore.JSStringRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectGetProperty, JavaScriptCore.JSValueRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetProperty,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetProperty,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetProperty,
            2,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetProperty,
            3,
            b"o^" + JavaScriptCore.JSObjectRef.__typestr__,
        )

        self.assertResultHasType(JavaScriptCore.JSObjectSetProperty, objc._C_VOID)
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetProperty,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetProperty,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetProperty,
            2,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetProperty, 3, JavaScriptCore.JSValueRef.__typestr__
        )
        self.assertArgHasType(JavaScriptCore.JSObjectSetProperty, 4, objc._C_UINT)
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetProperty,
            5,
            b"o^" + JavaScriptCore.JSObjectRef.__typestr__,
        )

        self.assertResultHasType(JavaScriptCore.JSObjectDeleteProperty, objc._C_BOOL)
        self.assertArgHasType(
            JavaScriptCore.JSObjectDeleteProperty,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectDeleteProperty,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectDeleteProperty,
            2,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectDeleteProperty,
            3,
            b"o^" + JavaScriptCore.JSObjectRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectGetPropertyAtIndex,
            JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetPropertyAtIndex,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetPropertyAtIndex,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(JavaScriptCore.JSObjectGetPropertyAtIndex, 2, objc._C_UINT)
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetPropertyAtIndex,
            3,
            b"o^" + JavaScriptCore.JSObjectRef.__typestr__,
        )

        self.assertResultHasType(JavaScriptCore.JSObjectSetPropertyAtIndex, objc._C_VOID)
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetPropertyAtIndex,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetPropertyAtIndex,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(JavaScriptCore.JSObjectSetPropertyAtIndex, 2, objc._C_UINT)
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetPropertyAtIndex,
            3,
            JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetPropertyAtIndex,
            4,
            b"o^" + JavaScriptCore.JSObjectRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectGetPrivate, objc._C_PTR + objc._C_VOID
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectGetPrivate, 0, JavaScriptCore.JSObjectRef.__typestr__
        )

        self.assertResultHasType(JavaScriptCore.JSObjectSetPrivate, objc._C_BOOL)
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetPrivate, 0, JavaScriptCore.JSObjectRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectSetPrivate, 1, objc._C_PTR + objc._C_VOID
        )

        self.assertResultHasType(JavaScriptCore.JSObjectIsFunction, objc._C_BOOL)
        self.assertArgHasType(
            JavaScriptCore.JSObjectIsFunction,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectIsFunction, 1, JavaScriptCore.JSObjectRef.__typestr__
        )

        self.assertResultHasType(JavaScriptCore.JSObjectIsConstructor, objc._C_BOOL)
        self.assertArgHasType(
            JavaScriptCore.JSObjectIsConstructor,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectIsConstructor,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectCopyPropertyNames,
            JavaScriptCore.JSPropertyNameArrayRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectCopyPropertyNames,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectCopyPropertyNames,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSPropertyNameArrayRetain,
            JavaScriptCore.JSPropertyNameArrayRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSPropertyNameArrayRetain,
            0,
            JavaScriptCore.JSPropertyNameArrayRef.__typestr__,
        )

        self.assertArgHasType(
            JavaScriptCore.JSPropertyNameArrayRelease,
            0,
            JavaScriptCore.JSPropertyNameArrayRef.__typestr__,
        )

        SIZE_T = objc._C_ULNG_LNG

        self.assertResultHasType(JavaScriptCore.JSPropertyNameArrayGetCount, SIZE_T)
        self.assertArgHasType(
            JavaScriptCore.JSPropertyNameArrayGetCount,
            0,
            JavaScriptCore.JSPropertyNameArrayRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSPropertyNameArrayGetNameAtIndex,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSPropertyNameArrayGetNameAtIndex,
            0,
            JavaScriptCore.JSPropertyNameArrayRef.__typestr__,
        )
        self.assertArgHasType(JavaScriptCore.JSPropertyNameArrayGetNameAtIndex, 1, SIZE_T)

        self.assertArgHasType(
            JavaScriptCore.JSPropertyNameAccumulatorAddName,
            0,
            JavaScriptCore.JSPropertyNameAccumulatorRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSPropertyNameAccumulatorAddName,
            1,
            JavaScriptCore.JSStringRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectCallAsFunction, JavaScriptCore.JSValueRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectCallAsFunction,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectCallAsFunction,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectCallAsFunction,
            2,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(JavaScriptCore.JSObjectCallAsFunction, 3, SIZE_T)
        self.assertArgHasType(
            JavaScriptCore.JSObjectCallAsFunction,
            4,
            b"n^" + JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgSizeInArg(JavaScriptCore.JSObjectCallAsFunction, 4, 3)
        self.assertArgHasType(
            JavaScriptCore.JSObjectCallAsFunction,
            5,
            b"o^" + JavaScriptCore.JSObjectRef.__typestr__,
        )

        self.assertResultHasType(
            JavaScriptCore.JSObjectCallAsConstructor,
            JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectCallAsConstructor,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectCallAsConstructor,
            1,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(JavaScriptCore.JSObjectCallAsConstructor, 2, SIZE_T)
        self.assertArgHasType(
            JavaScriptCore.JSObjectCallAsConstructor,
            3,
            b"n^" + JavaScriptCore.JSValueRef.__typestr__,
        )
        self.assertArgSizeInArg(JavaScriptCore.JSObjectCallAsConstructor, 3, 2)
        self.assertArgHasType(
            JavaScriptCore.JSObjectCallAsConstructor,
            4,
            b"o^" + JavaScriptCore.JSObjectRef.__typestr__,
        )

    def test_functions(self):
        self.assertResultHasType(
            JavaScriptCore.JSObjectMakeConstructor,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeConstructor,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeConstructor,
            1,
            JavaScriptCore.JSClassRef.__typestr__,
        )
        self.assertArgIsFunction(
            JavaScriptCore.JSObjectMakeConstructor,
            2,
            b"".join(
                [
                    JavaScriptCore.JSObjectRef.__typestr__,
                    JavaScriptCore.JSContextRef.__typestr__,
                    JavaScriptCore.JSObjectRef.__typestr__,
                    objc._C_ULNG,
                    b"n^" + JavaScriptCore.JSObjectRef.__typestr__,
                    b"o^" + JavaScriptCore.JSValueRef.__typestr__,
                ]
            ),
            True,
        )

        @objc.callbackFor(JavaScriptCore.JSObjectMakeConstructor)
        def constructor(ctx, constr, argumentCount, arguments, exception):
            return None

        self.assertArgSizeInArg(constructor, 3, 2)
        self.assertArgIsIn(constructor, 3)
        self.assertArgIsOut(constructor, 4)

        self.assertResultHasType(
            JavaScriptCore.JSObjectMakeFunctionWithCallback,
            JavaScriptCore.JSObjectRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeFunctionWithCallback,
            0,
            JavaScriptCore.JSContextRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSObjectMakeFunctionWithCallback,
            1,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgIsFunction(
            JavaScriptCore.JSObjectMakeFunctionWithCallback,
            2,
            b"".join(
                [
                    JavaScriptCore.JSValueRef.__typestr__,
                    JavaScriptCore.JSContextRef.__typestr__,
                    JavaScriptCore.JSObjectRef.__typestr__,
                    JavaScriptCore.JSObjectRef.__typestr__,
                    objc._C_ULNG,
                    b"n^" + JavaScriptCore.JSObjectRef.__typestr__,
                    b"o^" + JavaScriptCore.JSValueRef.__typestr__,
                ]
            ),
            True,
        )

        @objc.callbackFor(JavaScriptCore.JSObjectMakeFunctionWithCallback)
        def func(ctx, function, thisObject, argumentCount, arguments, exception):
            return None

        self.assertArgSizeInArg(func, 4, 3)
        self.assertArgIsIn(func, 4)
        self.assertArgIsOut(func, 5)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertArgIsOut(JavaScriptCore.JSObjectMakeDeferredPromise, 1)
        self.assertArgIsOut(JavaScriptCore.JSObjectMakeDeferredPromise, 2)
        self.assertArgIsOut(JavaScriptCore.JSObjectMakeDeferredPromise, 3)

        self.assertArgIsOut(JavaScriptCore.JSObjectHasPropertyForKey, 3)

        self.assertArgIsOut(JavaScriptCore.JSObjectGetPropertyForKey, 3)

        self.assertArgIsOut(JavaScriptCore.JSObjectSetPropertyForKey, 5)

        self.assertArgIsOut(JavaScriptCore.JSObjectDeletePropertyForKey, 3)

    def testUnsupported(self):
        self.assertNotHasAttr(JavaScriptCore, "kJSClassDefinitionEmpty")
        self.assertNotHasAttr(JavaScriptCore, "JSStaticValue")
        self.assertNotHasAttr(JavaScriptCore, "JSStaticFunction")
        self.assertNotHasAttr(JavaScriptCore, "JSClassDefinition")

        self.assertNotHasAttr(JavaScriptCore, "JSClassCreate")
