from PyObjCTools.TestSupport import *
import Cocoa
from PyObjCTools import AppHelper

class TestAppHelper (TestCase):
    def test_callAfter(self):
        pass

    def test_callLater(self):
        pass

    def test_stopEventLoop(self):
        pass

    def test_endSheetMethod(self):
        v = AppHelper.endSheetMethod(lambda x: None)
        self.assertEqual(v.signature, b'v@:@' + objc._C_NSInteger + objc._C_NSInteger)

    def test_runConsoleEventLoop(self):
        pass

    def test_runEventLoop(self):
        pass

if __name__ == "__main__":
    main()
