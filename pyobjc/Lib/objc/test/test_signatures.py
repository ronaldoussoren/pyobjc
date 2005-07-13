"""
Test some basic features of signature strings.
"""
import unittest
import objc

class PyOCTestTypeStr(unittest.TestCase):
    def testSelectorSignatures(self):

        self.assert_(
            isinstance(
                objc.selector(lambda(x,y):1, signature="ii"),
                objc.selector
            )
        )
        self.assert_(
            isinstance(
                objc.selector(lambda(x,y):1, argumentTypes="ii"),
                objc.selector
            )
        )
        self.assert_(
            isinstance(
                objc.selector(lambda(x,y):1,
                    argumentTypes="ii", returnType="s"),
                objc.selector
            )
        )

        self.assertRaises(ValueError, objc.selector, lambda (x,y):1,
                signature="FOOBAR")

        self.assertRaises(TypeError, objc.selector, lambda(x,y):1,
                signature="@@", returnType="i")
        self.assertRaises(TypeError, objc.selector, lambda(x,y):1,
                signature="@@", argumentTypes="ii")

        self.assertRaises(ValueError, objc.selector, lambda(x,y):1,
                argumentTypes="iX")
        self.assertRaises(ValueError, objc.selector, lambda(x,y):1,
                returnType="X")

    def testArgumentTypesPythonStyle(self):
        # Check that argumentTypes + returnType is correctly converted to
        # a signature

        s = objc.selector(lambda self: None, argumentTypes='ii', returnType='i')
        self.assertEquals(s.signature, 'i@:ii')

        s = objc.selector(lambda self: None, argumentTypes='Oi', returnType='i')
        self.assertEquals(s.signature, 'i@:@i')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='l')
        self.assertEquals(s.signature, objc._C_LNG + '@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='f')
        self.assertEquals(s.signature, objc._C_FLT + '@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='d')
        self.assertEquals(s.signature, objc._C_DBL + '@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='i')
        self.assertEquals(s.signature, objc._C_INT + '@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='s')
        self.assertEquals(s.signature, '@@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='S')
        self.assertEquals(s.signature, '@@:')

        s = objc.selector(lambda self: None, argumentTypes='', returnType='z')
        self.assertEquals(s.signature, '@@:')

        s = objc.selector(lambda self: None, argumentTypes='zbhilcfdO', returnType='z')
        self.assertEquals(s.signature, '@@:@csilcfd@')


    def testAll(self):
        if hasattr(objc, '_C_BOOL'):
            self.assertEquals(objc._C_BOOL, "B")
        self.assertEquals(objc._C_ID, "@")
        self.assertEquals(objc._C_CLASS, "#")
        self.assertEquals(objc._C_SEL, ":")
        self.assertEquals(objc._C_CHR, "c")
        self.assertEquals(objc._C_UCHR, "C")
        self.assertEquals(objc._C_SHT, "s")
        self.assertEquals(objc._C_USHT, "S")
        self.assertEquals(objc._C_INT, "i")
        self.assertEquals(objc._C_UINT, "I")
        self.assertEquals(objc._C_LNG, "l")
        self.assertEquals(objc._C_ULNG, "L")
        self.assertEquals(objc._C_LNGLNG, "q")
        self.assertEquals(objc._C_ULNGLNG, "Q")
        self.assertEquals(objc._C_FLT, "f")
        self.assertEquals(objc._C_DBL, "d")
        self.assertEquals(objc._C_VOID, "v")
        self.assertEquals(objc._C_CHARPTR, "*")
        self.assertEquals(objc._C_PTR, "^")
        self.assertEquals(objc._C_UNDEF, "?")
        self.assertEquals(objc._C_ARY_B, "[")
        self.assertEquals(objc._C_ARY_E, "]")
        self.assertEquals(objc._C_UNION_B, "(")
        self.assertEquals(objc._C_UNION_E, ")")
        self.assertEquals(objc._C_STRUCT_B, "{")
        self.assertEquals(objc._C_STRUCT_E, "}")
        self.assertEquals(objc._C_IN, "n")
        self.assertEquals(objc._C_OUT, "o")
        self.assertEquals(objc._C_INOUT, "N")

if __name__ == '__main__':
    unittest.main()
