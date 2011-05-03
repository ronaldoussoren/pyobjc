from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSScriptCommandDescriptionHelper (NSScriptCommandDescription):
    def isOptionalArgumentWithName_(self, name): return 1

class NSScriptCommandDescription (TestCase):
    def testMethods(self):
        # This should be tested on the actual NSScriptCommandDescription class,
        # but for some reason that class doesn't seem to have the
        # required method (at least not without instantating the class)
        self.assertResultIsBOOL(TestNSScriptCommandDescriptionHelper.isOptionalArgumentWithName_)

if __name__ == "__main__":
    main()
