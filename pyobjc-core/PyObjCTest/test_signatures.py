"""
Test some basic features of signature strings.
"""
from PyObjCTools.TestSupport import *
import objc

class PyOCTestTypeStr(TestCase):
    def testSelectorSignatures(self):
        self.assertRaises(ValueError, objc.selector, lambda x,y:1,
                signature=b"FOOBAR")

    def testAll(self):
        self.assertEqual(objc._C_BOOL, b"B")
        self.assertEqual(objc._C_ID, b"@")
        self.assertEqual(objc._C_CLASS, b"#")
        self.assertEqual(objc._C_SEL, b":")
        self.assertEqual(objc._C_CHR, b"c")
        self.assertEqual(objc._C_UCHR, b"C")
        self.assertEqual(objc._C_SHT, b"s")
        self.assertEqual(objc._C_USHT, b"S")
        self.assertEqual(objc._C_INT, b"i")
        self.assertEqual(objc._C_UINT, b"I")
        self.assertEqual(objc._C_LNG, b"l")
        self.assertEqual(objc._C_ULNG, b"L")
        self.assertEqual(objc._C_LNG_LNG, b"q")
        self.assertEqual(objc._C_ULNG_LNG, b"Q")
        self.assertEqual(objc._C_FLT, b"f")
        self.assertEqual(objc._C_DBL, b"d")
        self.assertEqual(objc._C_VOID, b"v")
        self.assertEqual(objc._C_CHARPTR, b"*")
        self.assertEqual(objc._C_PTR, b"^")
        self.assertEqual(objc._C_UNDEF, b"?")
        self.assertEqual(objc._C_ARY_B, b"[")
        self.assertEqual(objc._C_ARY_E, b"]")
        self.assertEqual(objc._C_UNION_B, b"(")
        self.assertEqual(objc._C_UNION_E, b")")
        self.assertEqual(objc._C_STRUCT_B, b"{")
        self.assertEqual(objc._C_STRUCT_E, b"}")
        self.assertEqual(objc._C_IN, b"n")
        self.assertEqual(objc._C_OUT, b"o")
        self.assertEqual(objc._C_INOUT, b"N")

    def testNativeSignature(self):
        s = objc.selector(lambda x,y:1, signature=b"ii")
        self.assertEqual(s.native_signature, b"ii")

        self.assertRaises((TypeError, AttributeError), setattr, s, 'native_signature', b'v@:ii')

        s = objc.lookUpClass('NSObject').description
        self.assertRaises((TypeError, AttributeError), setattr, s, 'native_signature', b'v@:ii')

        # We know that the description signature isn't changed by default
        self.assertEqual(s.signature, s.native_signature)

        # Check that changing s.signature doesn't affect s.native_signature
        try:
            x = s.signature
            s.signature = b'v@:ii'
            self.assertEqual(s.native_signature, x)
            self.assertEqual(s.signature, b'v@:ii')
        finally:
            s.signature = x


if __name__ == '__main__':
    main()
