import unittest
import objc
from objc.test.testoutputinitializer import PyObjC_TestOutputInitializer
objc.setSignatureForSelector("PyObjC_TestOutputInitializer", "initWithBooleanOutput:", "@@:o^c");

class TestOutputInitializer(unittest.TestCase):
    def testOutputInitializer(self):
        robj, rtrue = PyObjC_TestOutputInitializer.alloc().initWithBooleanOutput_()
        self.assertEquals(rtrue, objc.YES)
        self.assertEquals(robj.isInitialized(), objc.YES)

if __name__ == '__main__':
    unittest.main()
