import unittest

import Foundation

class GlobalFunctionTest (unittest.TestCase):
    
    def testMakeNSRect(self):
        self.assert_(hasattr(Foundation, 'NSMakeRect'))

        self.assertEquals(
                Foundation.NSMakeRect(1.5, 2.5, 3.5, 4.5), 
                ((1.5, 2.5), (3.5, 4.5))
        )
        self.assertEquals(
                Foundation.NSMakeRect(1, 2, 3, 4), 
                ((1.0, 2.0), (3.0, 4.0))
        )

        self.assertRaises(TypeError, Foundation.NSMakeRect, 1.0, 2.0, 3.0, '4')

    def testMisc(self):
        self.assert_(hasattr(Foundation, 'NSLogPageSize'))
        self.assert_(hasattr(Foundation, 'NSRangeFromString'))
        self.assert_(hasattr(Foundation, 'NSTemporaryDirectory'))
        self.assert_(hasattr(Foundation, 'NSDecrementExtraRefCountWasZero'))

class GlobalVariablesTest (unittest.TestCase):
    def testMisc(self):
        # enum
        self.assert_(hasattr(Foundation, 'NS_LittleEndian'))
        self.assert_(hasattr(Foundation, 'NSXMLParserExtraContentError'))

        # NSString
        self.assert_(hasattr(Foundation, 'NSAppleScriptErrorNumber'))
        self.assert_(hasattr(Foundation, 'NSConnectionReplyMode'))

        # VAR
        self.assert_(hasattr(Foundation, 'NSFoundationVersionNumber'))

if __name__ == "__main__":
    unittest.main()

