import objc.test
from objc.test.protected import *

class TestProtected (objc.test.TestCase):
    def testProtectedNotInDir(self):

        d = dir(PyObjCTest_Protected)
        self.assert_( 'publicMethod' in d )
        self.assert_( '_protectedMethod' not in d )

    def testProtectedCallable(self):
        o = PyObjCTest_Protected.new()
        self.assertEquals(None, o._protectedMethod())
        self.assertEquals(None, o.publicMethod())

if __name__ == "__main__":
    objc.test.main()
