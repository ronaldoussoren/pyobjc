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


    @expectedFailure
    def testMisc(self):
        self.fail("Actually test this module")
        # - isPythonException
        # - nsLogPythonException
        # - nsLogObjCException
        #
        # - Actually trigger handler in various modes

if __name__ == "__main__":
    main()
