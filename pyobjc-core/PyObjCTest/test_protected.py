from PyObjCTools.TestSupport import *
from PyObjCTest.protected import *

class TestProtected (TestCase):

    # XXX: this functionaly has been removed
    #      either readd, or remove test
    @expectedFailure    
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
