from PyObjCTest.protected import PyObjCTest_Protected
from PyObjCTools.TestSupport import TestCase


class TestProtected(TestCase):
    def testProtectedCallable(self):
        o = PyObjCTest_Protected.new()
        self.assertEqual(None, o._protectedMethod())
        self.assertEqual(None, o.publicMethod())
