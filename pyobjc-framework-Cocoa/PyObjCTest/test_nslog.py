import os

import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSLog(TestCase):
    def _redirect(self):
        fd = os.open("pyobjc-test-nslog.txt", os.O_RDWR | os.O_CREAT, 0o666)
        self.real_stderr = os.dup(2)
        os.dup2(fd, 2)
        os.close(fd)

    def _cleanup(self):
        os.dup2(self.real_stderr, 2)
        fp = open("pyobjc-test-nslog.txt", "rb")
        data = fp.read()
        fp.close()
        os.unlink("pyobjc-test-nslog.txt")
        return data

    def testBasic(self):
        self._redirect()
        try:
            Foundation.NSLog("Hello world")
        finally:
            data = self._cleanup().rstrip()

        self.assertTrue(data.endswith(b"] Hello world"))

    def testWithArguments(self):
        self._redirect()
        try:
            Foundation.NSLog("Hello %@: the count is %d", "ronald", 99)
        finally:
            data = self._cleanup().rstrip()

        self.assertTrue(data.endswith(b"] Hello ronald: the count is 99"))

    def testWithInvalidFormat(self):
        self._redirect()
        try:
            self.assertRaises(
                ValueError, Foundation.NSLog, "Hello %@: the count is %d", "ronald"
            )
            self.assertRaises(
                ValueError,
                Foundation.NSLog,
                "Hello %@: the count is %d",
                "ronald",
                "foo",
            )
            self.assertRaises(
                ValueError,
                Foundation.NSLog,
                "Hello %@: the count is %d",
                "ronald",
                42,
                "foo",
            )

        finally:
            self._cleanup()


class TestNSLogv(TestCase):
    def testNotSuchThing(self):
        self.assertFalse(hasattr(Foundation, "NSLogv"))
