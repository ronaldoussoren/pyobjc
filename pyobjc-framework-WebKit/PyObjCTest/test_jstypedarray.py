from PyObjCTools.TestSupport import *

import JavaScriptCore
import objc

class TestJSTypedArray (TestCase):
    @min_os_level('10.12')
    def test_functions(self):
        self.assertResultHasType(JavaScriptCore.JSObjectMakeTypedArray, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArray, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArray, 1, objc._C_INT)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArray, 2, objc._C_ULNG) # size_t
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArray, 3, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectMakeTypedArrayWithBytesNoCopy, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithBytesNoCopy, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithBytesNoCopy, 1, objc._C_INT)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithBytesNoCopy, 2, b'n^v')
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithBytesNoCopy, 3, objc._C_ULNG) # size_t
        self.assertArgIsFunction(JavaScriptCore.JSObjectMakeTypedArrayWithBytesNoCopy, 4, b'vn^v^v', True)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithBytesNoCopy, 5, b'^v')
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithBytesNoCopy, 6, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBuffer, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBuffer, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBuffer, 1, objc._C_INT)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBuffer, 2, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBuffer, 3, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBufferAndOffset, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBufferAndOffset, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBufferAndOffset, 1, objc._C_INT)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBufferAndOffset, 2, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBufferAndOffset, 3, objc._C_ULNG)  # size_t
        self.assertArgHasType(JavaScriptCore.JSObjectMakeTypedArrayWithArrayBufferAndOffset, 4, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectGetTypedArrayBytesPtr, b'^v')
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayBytesPtr, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayBytesPtr, 1, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayBytesPtr, 2, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectGetTypedArrayLength, objc._C_ULNG) # size_t
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayLength, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayLength, 1, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayLength, 2, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectGetTypedArrayByteLength, objc._C_ULNG) # size_t
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayByteLength, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayByteLength, 1, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayByteLength, 2, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectGetTypedArrayByteOffset, objc._C_ULNG) # size_t
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayByteOffset, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayByteOffset, 1, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayByteOffset, 2, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectGetTypedArrayBuffer, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayBuffer, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayBuffer, 1, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetTypedArrayBuffer, 2, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectMakeArrayBufferWithBytesNoCopy, JavaScriptCore.JSObjectRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeArrayBufferWithBytesNoCopy, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeArrayBufferWithBytesNoCopy, 1, b'n^v')
        self.assertArgHasType(JavaScriptCore.JSObjectMakeArrayBufferWithBytesNoCopy, 2, objc._C_ULNG) # size_t
        self.assertArgIsFunction(JavaScriptCore.JSObjectMakeArrayBufferWithBytesNoCopy, 3, b'vn^v^v', True)
        self.assertArgHasType(JavaScriptCore.JSObjectMakeArrayBufferWithBytesNoCopy, 4, b'^v')
        self.assertArgHasType(JavaScriptCore.JSObjectMakeArrayBufferWithBytesNoCopy, 5, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectGetArrayBufferBytesPtr, b'^v')
        self.assertArgHasType(JavaScriptCore.JSObjectGetArrayBufferBytesPtr, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetArrayBufferBytesPtr, 1, JavaScriptCore.JSValueRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetArrayBufferBytesPtr, 2, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

        self.assertResultHasType(JavaScriptCore.JSObjectGetArrayBufferByteLength, b'L')
        self.assertArgHasType(JavaScriptCore.JSObjectGetArrayBufferByteLength, 0, JavaScriptCore.JSContextRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetArrayBufferByteLength, 1, JavaScriptCore.JSValueRef.__typestr__)
        self.assertArgHasType(JavaScriptCore.JSObjectGetArrayBufferByteLength, 2, b'o^' + JavaScriptCore.JSValueRef.__typestr__)

if __name__ == "__main__":
    main()
