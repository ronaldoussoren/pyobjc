from PyObjCTools.TestSupport import *
from PyObjCTest.protected import *

class TestProtected (TestCase):
    def testProtectedNotInDir(self):

        d = dir(PyObjCTest_Protected)
        self.assertIn('publicMethod', d)
        self.assertNotIn('_protectedMethod', d)

    def testProtectedCallable(self):
        o = PyObjCTest_Protected.new()
        self.assertEqual(None, o._protectedMethod())
        self.assertEqual(None, o.publicMethod())

if __name__ == "__main__":
    PyObjCTest.main()
