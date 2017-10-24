'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import sys
from PyObjCTools.TestSupport import *
from PyObjCTools import Debugging

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

        else:
            self.fail("Exception not raised")


        try:
            cls = objc.lookUpClass('NSException')
            cls.exceptionWithName_reason_userInfo_('FooBar', 'hello world', None).raise__()
        except Exception as exc:
            self.assertFalse(Debugging.isPythonException(exc))

        else:
            self.fail("Exception not raised")

        try:
            a = []
            a[42]

        except Exception as exc:
            self.assertTrue(Debugging.isPythonException(exc))

    @expectedFailureIf(sys.byteorder == 'big')
    def testAtos(self):
        NSThread = objc.lookUpClass('NSThread')
        v = ' '.join(hex(x) for x in NSThread.callStackReturnAddresses())
        fp = Debugging._run_atos(v)
        value = fp.read()
        fp.close()

        self.assertIn('_objc.', value)

    def testInstallExceptionHandler(self):
        self.assertFalse(Debugging.handlerInstalled())
        try:
            Debugging.installExceptionHandler(verbosity=Debugging.LOGSTACKTRACE, mask=Debugging.EVERYTHINGMASK)
            self.assertTrue(Debugging.handlerInstalled())

            try:
                cls = objc.lookUpClass('NSException')
                cls.exceptionWithName_reason_userInfo_('FooBar', 'hello world', None).raise__()
            except Exception as exc:
                self.assertFalse(Debugging.isPythonException(exc))

            else:
                self.fail("Exception not raised")

            try:
                cls = objc.lookUpClass('NSArray')

                def test(value, idx, stop):
                    raise ValueError("42")
                a = cls.alloc().initWithArray_([1,2,3,4])
                a.indexOfObjectPassingTest_(test)


            except Exception as exc:
                self.assertTrue(Debugging.isPythonException(exc))

            else:
                self.fail("Exception not raised")

        finally:
            Debugging.removeExceptionHandler()
            self.assertFalse(Debugging.handlerInstalled())

    @expectedFailure
    def testMisc(self):
        self.fail("Actually test this module")
        # - nsLogPythonException
        # - nsLogObjCException
        #
        # - Actually trigger handler in various modes

if __name__ == "__main__":
    main()
