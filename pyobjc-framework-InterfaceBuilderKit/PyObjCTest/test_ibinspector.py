
from PyObjCTools.TestSupport import *
from InterfaceBuilderKit import *

class TestIBInspector (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(IBInspector.supportsMultipleObjectInspection)

if __name__ == "__main__":
    main()
