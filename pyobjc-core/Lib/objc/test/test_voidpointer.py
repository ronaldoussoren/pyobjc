import objc.test, sys
from objc.test.voidpointer import OC_TestVoidPointer

class TestVoidPointer (objc.test.TestCase):
    def testVoidPointerMethods(self):
        o = OC_TestVoidPointer.alloc().init()
        self.assertEquals(o.getvalue(), 0)

        o.setvalue_(523532)
        self.assertEquals(o.getvalue(), 523532)

        o.setvalue_(sys.maxint + 1)
        self.assertEquals(o.getvalue(), sys.maxint + 1)

if __name__ == "__main__":
    objc.test.main()

