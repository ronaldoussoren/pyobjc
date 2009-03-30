from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSScriptCoercionHandler (TestCase):
    def testMethods(self):
        self.failUnlessArgIsSEL(NSScriptCoercionHandler.registerCoercer_selector_toConvertFromClass_toClass_, 1, '@@:@#')

if __name__ == "__main__":
    main()
