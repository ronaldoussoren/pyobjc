'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import ExceptionHandling

class TestExceptionHandling (unittest.TestCase):
    def testClasses(self):
        self.assert_(hasattr(ExceptionHandling, 'NSExceptionHandler'))
        self.assert_(isinstance(ExceptionHandling.NSExceptionHandler, objc.objc_class))

    def testValues(self):
        self.assert_( hasattr(ExceptionHandling, 'NSLogUncaughtExceptionMask') )
        self.assert_( isinstance(ExceptionHandling.NSLogUncaughtExceptionMask, (int, long)) )
        self.assertEquals(ExceptionHandling.NSLogUncaughtExceptionMask, 1)

        self.assert_( hasattr(ExceptionHandling, 'NSLogOtherExceptionMask') )
        self.assert_( isinstance(ExceptionHandling.NSLogOtherExceptionMask, (int, long)) )

        self.assertEquals(ExceptionHandling.NSLogOtherExceptionMask, 1 << 8)

        self.assert_( hasattr(ExceptionHandling, 'NSLogAndHandleEveryExceptionMask') )
        self.assert_( isinstance(ExceptionHandling.NSLogAndHandleEveryExceptionMask, (int, long)) )

        self.assert_( hasattr(ExceptionHandling, 'NSHangOnEveryExceptionMask') )
        self.assert_( isinstance(ExceptionHandling.NSHangOnEveryExceptionMask, (int, long)) )


    def testVariables(self):
        self.assert_( hasattr(ExceptionHandling, 'NSUncaughtSystemExceptionException') )
        self.assert_( isinstance(ExceptionHandling.NSUncaughtSystemExceptionException, unicode) )

    def testProtocols(self):
        self.assert_( hasattr(ExceptionHandling, 'protocols') )

        self.assert_( hasattr(ExceptionHandling.protocols, 'NSExceptionHandlerDelegate') )
        self.assert_( isinstance(ExceptionHandling.protocols.NSExceptionHandlerDelegate, objc.informal_protocol) )

if __name__ == "__main__":
    unittest.main()

