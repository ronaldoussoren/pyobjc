import unittest
import objc
from testclassandinst import PyObjC_TestClassAndInstance

class TestClassAndInstance(unittest.TestCase):
    def testClassAndInstance(self):
        self.assertEquals(PyObjC_TestClassAndInstance.isInstance(), objc.NO)
        self.assertEquals(PyObjC_TestClassAndInstance.alloc().init().isInstance(), objc.YES)

if __name__ == '__main__':
    unittest.main()
