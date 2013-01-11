'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
from PyObjCTools import Debugging

try:
    long
except NameError:
    long = int

class TestDebugging (TestCase):
    def testConstants(self):
        for nm in (
                'LOGSTACKTRACE', 'DEFAULTVERBOSITY',
                'DEFAULTMASK', 'EVERYTHINGMASK'):
            self.assertTrue(hasattr(Debugging, nm))
            self.assertTrue(isinstance(getattr(Debugging, nm), (int, long)))

    def testHandlerBasic(self):
        self.assertFalse(Debugging.handlerInstalled())

        Debugging.installExceptionHandler()
        self.assertTrue(Debugging.handlerInstalled())

        Debugging.removeExceptionHandler()
        self.assertFalse(Debugging.handlerInstalled())

        Debugging.installVerboseExceptionHandler()
        self.assertTrue(Debugging.handlerInstalled())

        Debugging.removeExceptionHandler()
        self.assertFalse(Debugging.handlerInstalled())

        Debugging.installPythonExceptionHandler()
        self.assertTrue(Debugging.handlerInstalled())

        Debugging.removeExceptionHandler()
        self.assertFalse(Debugging.handlerInstalled())

    def test_isPythonException(self):
        try:
            a = objc.lookUpClass('NSArray').array()
            a.objectAtIndex_(42)
        except Exception as exc:
            self.assertFalse(Debugging.isPythonException(exc))

        try:
            a = []
            a[42]

        except Exception as exc:
            self.assertTrue(Debugging.isPythonException(exc))

    @expectedFailure
    def testMisc(self):
        self.fail("Actually test this module")
        # - nsLogPythonException
        # - nsLogObjCException
        #
        # - Actually trigger handler in various modes

if __name__ == "__main__":
    main()
