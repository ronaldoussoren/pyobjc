import objc
from PyObjCTest.testoutputinitializer import PyObjC_TestOutputInitializer
from PyObjCTools.TestSupport import TestCase

objc.registerMetaDataForSelector(
    b"PyObjC_TestOutputInitializer",
    b"initWithBooleanOutput:",
    {"arguments": {2: {"type_modifier": b"o"}}},
)


class TestOutputInitializer(TestCase):
    def testOutputInitializer(self):
        robj, rtrue = PyObjC_TestOutputInitializer.alloc().initWithBooleanOutput_(None)
        self.assertEqual(rtrue, objc.YES)
        self.assertEqual(robj.isInitialized(), objc.YES)
