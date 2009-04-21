
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
        self.failUnlessArgHasType(TestWebScriptObjectHelper.webScriptNameForSelector_, 0, objc._C_SEL)
        self.failUnlessArgHasType(TestWebScriptObjectHelper.isSelectorExcludedFromWebScript_, 0, objc._C_SEL)
        self.failUnlessArgHasType(TestWebScriptObjectHelper.webScriptNameForKey_, 0, 'n^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessArgIsNullTerminated(TestWebScriptObjectHelper.webScriptNameForKey_, 0)
        self.failUnlessArgHasType(TestWebScriptObjectHelper.isKeyExcludedFromWebScript_, 0, 'n^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessArgIsNullTerminated(TestWebScriptObjectHelper.isKeyExcludedFromWebScript_, 0)

        self.failUnlessResultIsBOOL(WebScriptObject.throwException_)



if __name__ == "__main__":
    main()
