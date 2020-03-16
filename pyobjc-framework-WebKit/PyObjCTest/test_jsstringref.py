import JavaScriptCore
import objc
from PyObjCTools.TestSupport import TestCase


class TestJSBase(TestCase):
    def test_functions(self):
        self.assertResultHasType(
            JavaScriptCore.JSStringCreateWithCharacters,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSStringCreateWithCharacters, 0, b"n^" + objc._C_UNICHAR
        )
        self.assertArgSizeInArg(JavaScriptCore.JSStringCreateWithCharacters, 0, 1)

        self.assertResultHasType(
            JavaScriptCore.JSStringCreateWithUTF8CString,
            JavaScriptCore.JSStringRef.__typestr__,
        )
        self.assertArgHasType(
            JavaScriptCore.JSStringCreateWithUTF8CString,
            0,
            b"n^" + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(JavaScriptCore.JSStringCreateWithUTF8CString, 0)

        self.assertResultHasType(
            JavaScriptCore.JSStringRetain, JavaScriptCore.JSStringRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSStringRetain, 0, JavaScriptCore.JSStringRef.__typestr__
        )

        self.assertArgHasType(
            JavaScriptCore.JSStringRelease, 0, JavaScriptCore.JSStringRef.__typestr__
        )
        self.assertArgHasType(
            JavaScriptCore.JSStringGetLength, 0, JavaScriptCore.JSStringRef.__typestr__
        )

        val = JavaScriptCore.JSStringCreateWithUTF8CString(b"hello world")
        self.assertEqual(JavaScriptCore.JSStringGetLength(val), len("hello world"))
        self.assertTrue(
            JavaScriptCore.JSStringGetMaximumUTF8CStringSize(val)
            >= len("hello world") + 1
        )

        self.assertFalse(hasattr(JavaScriptCore, "JSStringGetCharactersPtr"))

        self.assertArgSizeInArg(JavaScriptCore.JSStringGetUTF8CString, 1, 2)
        self.assertArgSizeInResult(JavaScriptCore.JSStringGetUTF8CString, 1)
        self.assertArgIsOut(JavaScriptCore.JSStringGetUTF8CString, 1)

        self.assertResultHasType(JavaScriptCore.JSStringIsEqual, objc._C_BOOL)

        self.assertResultHasType(
            JavaScriptCore.JSStringIsEqualToUTF8CString, objc._C_BOOL
        )
        self.assertArgHasType(
            JavaScriptCore.JSStringIsEqualToUTF8CString, 1, b"n^" + objc._C_CHAR_AS_TEXT
        )
        self.assertArgIsNullTerminated(JavaScriptCore.JSStringIsEqualToUTF8CString, 1)
