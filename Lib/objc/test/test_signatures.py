"""
Test some basic features of signature strings.
"""
import unittest
import objc

class PyOCTestTypeStr(unittest.TestCase):
    def testAll(self):
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
