import unittest
import objc
import sys
import time


if "%02d%02d"%(sys.version_info[:2]) >= '0203':
    # On Python 2.3 and later we use the API from PEP311 to make it possible
    # to call back into python from arbitrary threads, including those that
    # are created by Cocoa.
    #

    # Make sure the interpreter is in 'multi-threaded mode', otherwise new
    # threads that are not created in Python will cause a crash.
    objc.enableThreading()

    class ThreadingTest (unittest.TestCase):
        def setUp(self):
            # Set a very small check interval, this will make it more likely
            # that the interpreter crashes when threading is done incorrectly.
            self._int = sys.getcheckinterval()
            sys.setcheckinterval(1)

        def tearDown(self):
            sys.setcheckinterval(self._int)

        def testNSObjectString(self):

            class PyObjCTestThreadRunnerString (objc.runtime.NSObject):
                def init(self):
                    self = super(PyObjCTestThreadRunnerString, self).init()
                    if self is None: return None

                    self.storage = []
                    return self

                def run_(self, argument):
                    objc.runtime.NSAutoreleasePool.alloc().init()
                    self.storage.append(argument)

            myObj = PyObjCTestThreadRunnerString.alloc().init()

            objc.runtime.NSThread.detachNewThreadSelector_toTarget_withObject_(
                    'run:', myObj, "hello world")

            time.sleep(2)
            self.assertEquals(myObj.storage[0], u"hello world")

        def testNSObject(self):

            class PyObjCTestThreadRunner (objc.runtime.NSObject):
                def run_(self, argument):
                    objc.runtime.NSAutoreleasePool.alloc().init()
                    for i in range(100):
                        argument.append(i)

            myObj = PyObjCTestThreadRunner.alloc().init()
            lst = []

            objc.runtime.NSThread.detachNewThreadSelector_toTarget_withObject_(
                    'run:', myObj, lst)

            lst2 = []
            for i in range(100):
                lst2.append(i*2)

            time.sleep(2)
            self.assertEquals(lst, range(100))

        def testPyObject(self):

            class TestThreadRunner :
                def run_(self, argument):
                    for i in range(100):
                        argument.append(i)

            myObj = TestThreadRunner()
            lst = []

            objc.runtime.NSThread.detachNewThreadSelector_toTarget_withObject_(
                    'run:', myObj, lst)

            lst2 = []
            for i in range(100):
                lst2.append(i*2)

            time.sleep(2)
            self.assertEquals(lst, range(100))


if __name__ == "__main__":
    unittest.main()
