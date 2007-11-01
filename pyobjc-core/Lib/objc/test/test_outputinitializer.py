import objc.test
import objc
from objc.test.testoutputinitializer import PyObjC_TestOutputInitializer

objc.registerMetaDataForSelector("PyObjC_TestOutputInitializer", 
        "initWithBooleanOutput:", dict(arguments={
            2: dict(type_modifier='o')}))

class TestOutputInitializer(objc.test.TestCase):
    def testOutputInitializer(self):
        robj, rtrue = PyObjC_TestOutputInitializer.alloc().initWithBooleanOutput_(None)
        self.assertEquals(rtrue, objc.YES)
        self.assertEquals(robj.isInitialized(), objc.YES)

if __name__ == '__main__':
    objc.test.main()
