"""
Some tests for NSFormatter, basically only checks for method signatures.
"""
import unittest
import objc
from Foundation import *

class TestFormatter (unittest.TestCase):
    def testFormatter(self):
        m = NSFormatter.isPartialStringValid_newEditingString_errorDescription_
        sig = objc.splitSignature(m.signature)
        self.assertEquals(list(sig),
                [objc._C_NSBOOL, objc._C_ID, objc._C_SEL,
                    objc._C_ID, objc._C_OUT + objc._C_PTR + objc._C_ID,
                    objc._C_OUT + objc._C_PTR + objc._C_ID])

        m = NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_
        sig = objc.splitSignature(m.signature)

        range_typestr = NSRange.__typestr__
        self.assertEquals(list(sig),
                [ objc._C_NSBOOL, objc._C_ID, objc._C_SEL,
                    objc._C_INOUT + objc._C_PTR + objc._C_ID,
                    objc._C_INOUT + objc._C_PTR + range_typestr,
                    objc._C_ID, range_typestr, 
                    objc._C_OUT + objc._C_PTR + objc._C_ID])


if __name__ == "__main__":
    unittest.main()
