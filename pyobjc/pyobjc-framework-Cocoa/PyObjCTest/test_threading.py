from PyObjCTools.TestSupport import *
import objc
import sys
import time

from PyObjCTest.testhelper import PyObjC_TestClass4

from Foundation import *

class ThreadingTest (TestCase):
    def setUp(self):
        # Set a very small check interval, this will make it more likely
        # that the interpreter crashes when threading is done incorrectly.
        if sys.version_info[:2] >= (3, 2):
            self._int = sys.getswitchinterval()
            sys.setswitchinterval(0.0000001)
        else:
            self._int = sys.getcheckinterval()
            sys.setcheckinterval(1)

    def tearDown(self):
        if sys.version_info[:2] >= (3, 2):
            sys.setswitchinterval(self._int)
        else:
            sys.setcheckinterval(self._int)

    def testNSObjectString(self):

        class PyObjCTestThreadRunnerString (NSObject):
            def init(self):
                self = super(PyObjCTestThreadRunnerString, self).init()
                if self is None: return None

                self.storage = []
                return self

            def run_(self, argument):
                NSAutoreleasePool.alloc().init()
                self.storage.append(argument)

        myObj = PyObjCTestThreadRunnerString.alloc().init()

        NSThread.detachNewThreadSelector_toTarget_withObject_(
                'run:', myObj, u"hello world")

        time.sleep(2)
        self.assertEqual(myObj.storage[0], u"hello world")

    def testNSObject(self):

        class PyObjCTestThreadRunner (NSObject):
            def run_(self, argument):
                NSAutoreleasePool.alloc().init()
                for i in range(100):
                    argument.append(i)

        myObj = PyObjCTestThreadRunner.alloc().init()
        lst = []

        NSThread.detachNewThreadSelector_toTarget_withObject_(
                'run:', myObj, lst)

        lst2 = []
        for i in range(100):
            lst2.append(i*2)

        time.sleep(2)
        self.assertEqual(lst, range(100))

    def testPyObject(self):
        import os

        class TestThreadRunner :
            def run_(self, argument):
                for i in range(100):
                    argument.append(i)

        myObj = TestThreadRunner()
        lst = []

        # Redirect stderr to avoid spurious messages when running the
        # tests.
        dupped = os.dup(2)
        fp = os.open('/dev/null', os.O_RDWR)
        os.dup2(fp, 2)
        os.close(fp)

        try:
            NSThread.detachNewThreadSelector_toTarget_withObject_(
                'run:', myObj, lst)

            lst2 = []
            for i in range(100):
                lst2.append(i*2)

            time.sleep(2)
            self.assertEqual(lst, range(100))

        finally:
            os.dup2(dupped, 2)

    def testCalling(self):
        class Dummy:
            pass
        class PyObjCTestCalling (NSObject) :
            def call(self):
                return Dummy()

        my = PyObjC_TestClass4.alloc().init()
        cb = PyObjCTestCalling.alloc().init()

        NSThread.detachNewThreadSelector_toTarget_withObject_(
                'runThread:', my,  cb)

        time.sleep(2)

        retval = my.returnObject()
        self.assert_(isinstance(retval, Dummy))

if __name__ == "__main__":
    main()
