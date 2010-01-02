from PyObjCTools.TestSupport import *
from PyObjCTest.protected import *

class TestProtected (TestCase):
    def testProtectedNotInDir(self):

        d = dir(PyObjCTest_Protected)
        self.assertIsIn('publicMethod', d)
        self.assertIsNotIn('_protectedMethod', d)

    def testProtectedCallable(self):
        o = PyObjCTest_Protected.new()
        self.assertEquals(None, o._protectedMethod())
        self.assertEquals(None, o.publicMethod())

if __name__ == "__main__":
    PyObjCTest.main()
