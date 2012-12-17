from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.testoutputinitializer import PyObjC_TestOutputInitializer

objc.registerMetaDataForSelector(b"PyObjC_TestOutputInitializer",
        b"initWithBooleanOutput:", dict(arguments={
            2: dict(type_modifier=b'o')}))

class TestOutputInitializer(TestCase):
    def testOutputInitializer(self):
        robj, rtrue = PyObjC_TestOutputInitializer.alloc().initWithBooleanOutput_(None)
        self.assertEqual(rtrue, objc.YES)
        self.assertEqual(robj.isInitialized(), objc.YES)

if __name__ == '__main__':
    main()
