from PyObjCTools.TestSupport import *
import os
from Foundation import *
import Foundation

class TestNSLog (TestCase):
    def _redirect(self):
        fd = os.open('pyobjc-test-nslog.txt', os.O_RDWR|os.O_CREAT, 0o666)
        self.real_stderr = os.dup(2)
        os.dup2(fd, 2)
        os.close(fd)

    def _cleanup(self):
        os.dup2(self.real_stderr, 2)
        fp = open('pyobjc-test-nslog.txt', 'rb')
        data = fp.read()
        fp.close()
        os.unlink('pyobjc-test-nslog.txt')
        return data

    def testBasic(self):
        self._redirect()
        try:
            NSLog("Hello world")
        finally:
            data = self._cleanup().rstrip()

        self.assert_(data.endswith(b'] Hello world'))

    def testWithArguments(self):
        self._redirect()
        try:
            NSLog("Hello %@: the count is %d", "ronald", 99)
        finally:
            data = self._cleanup().rstrip()

        self.assert_(data.endswith(b'] Hello ronald: the count is 99'))

    def testWithInvalidFormat(self):
        self._redirect()
        try:
            self.assertRaises(ValueError, NSLog, "Hello %@: the count is %d", "ronald")
            self.assertRaises(ValueError, NSLog, "Hello %@: the count is %d", "ronald", "foo")
            self.assertRaises(ValueError, NSLog, "Hello %@: the count is %d", "ronald", 42, "foo")

        finally:
            data = self._cleanup().rstrip()

class TestNSLogv (TestCase):
    def testNotSuchThing(self):
        self.assert_(not hasattr(Foundation, 'NSLogv'))

if __name__ == "__main__":
    main()
