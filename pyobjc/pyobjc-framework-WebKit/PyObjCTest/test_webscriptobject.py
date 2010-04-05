
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebScriptObjectHelper (NSObject):
    @classmethod
    def webScriptNameForSelector_(self, sel): return 1

    @classmethod
    def isSelectorExcludedFromWebScript_(self, sel): return 1

    @classmethod
    def webScriptNameForKey_(self, name): return 1

    @classmethod
    def isKeyExcludedFromWebScript_(self, name): return 1

class TestWebScriptObject (TestCase):
    def testMethods(self):
        self.assertArgHasType(TestWebScriptObjectHelper.webScriptNameForSelector_, 0, objc._C_SEL)
        self.assertArgHasType(TestWebScriptObjectHelper.isSelectorExcludedFromWebScript_, 0, objc._C_SEL)
        self.assertArgHasType(TestWebScriptObjectHelper.webScriptNameForKey_, 0, b'n^' + objc._C_CHAR_AS_TEXT)
        self.assertArgIsNullTerminated(TestWebScriptObjectHelper.webScriptNameForKey_, 0)
        self.assertArgHasType(TestWebScriptObjectHelper.isKeyExcludedFromWebScript_, 0, b'n^' + objc._C_CHAR_AS_TEXT)
        self.assertArgIsNullTerminated(TestWebScriptObjectHelper.isKeyExcludedFromWebScript_, 0)

        self.assertResultIsBOOL(WebScriptObject.throwException_)



if __name__ == "__main__":
    main()
