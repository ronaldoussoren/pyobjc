
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMEventTargetHelper (NSObject):
    def addEventListener_listener_useCapture_(self, a, b, c): pass
    def removeEventListener_listener_useCapture_(self, a, b, c): pass
    def dispatchEvent_(self, a): return 1
    def addEventListener___(self, a, b, c): pass
    def removeEventListener___(self, a, b, c): pass

class TestDOMEventTarget (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(TestDOMEventTargetHelper.addEventListener_listener_useCapture_, 2)
        self.failUnlessArgIsBOOL(TestDOMEventTargetHelper.removeEventListener_listener_useCapture_, 2)
        self.failUnlessArgIsBOOL(TestDOMEventTargetHelper.addEventListener___, 2)
        self.failUnlessArgIsBOOL(TestDOMEventTargetHelper.removeEventListener___, 2)
        self.failUnlessResultIsBOOL(TestDOMEventTargetHelper.dispatchEvent_)

if __name__ == "__main__":
    main()
