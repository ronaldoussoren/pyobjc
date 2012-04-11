"""
Test some basic features of signature strings.
"""
from PyObjCTools.TestSupport import *
import objc

class PyOCTestTypeStr(TestCase):
    def testSelectorSignatures(self):

        self.assertIsInstance(
                objc.selector(lambda x,y:1, signature=b"ii"),
                objc.selector
        )
        self.assertIsInstance(
                objc.selector(lambda x,y:1, argumentTypes="ii"),
                objc.selector
        )
        self.assertIsInstance(
                objc.selector(lambda x,y:1,
                    argumentTypes="ii", returnType="s"),
                objc.selector
        )

        self.assertRaises(ValueError, objc.selector, lambda x,y:1,
                signature=b"FOOBAR")

        self.assertRaises(TypeError, objc.selector, lambda x,y:1,
                signature=b"@@", returnType="i")
        self.assertRaises(TypeError, objc.selector, lambda x,y:1,
                signature=b"@@", argumentTypes="ii")

        self.assertRaises(ValueError, objc.selector, lambda x,y:1,
                argumentTypes="iX")
        self.assertRaises(ValueError, objc.selector, lambda x,y:1,
                returnType="X")

    def testArgumentTypesPythonStyle(self):
        # Check that argumentTypes + returnType is correctly converted to
        # a signature

        s = objc.selector(lambda self: None, argumentTypes='ii', returnType='i')
        self.assertEqual(s.signature, b'i@:ii')

        s = objc.selector(lambda self: None, argumentTypes='Oi', returnType='i')
        self.assertEqual(s.signature, b'i@:@i')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='l')
        self.assertEqual(s.signature, objc._C_LNG + b'@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='f')
        self.assertEqual(s.signature, objc._C_FLT + b'@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='d')
        self.assertEqual(s.signature, objc._C_DBL + b'@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='i')
        self.assertEqual(s.signature, objc._C_INT + b'@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='s')
        self.assertEqual(s.signature, b'@@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='S')
        self.assertEqual(s.signature, b'@@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='z')
        self.assertEqual(s.signature, b'@@:')

        s = objc.selector(lambda self: None, argumentTypes='zbhilcfdO', returnType='z')
        self.assertEqual(s.signature, b'@@:@csilcfd@')


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
