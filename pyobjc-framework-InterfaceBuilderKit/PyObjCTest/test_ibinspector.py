from InterfaceBuilderKit import *
from PyObjCTools.TestSupport import *


class TestIBInspector(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(IBInspector.supportsMultipleObjectInspection)


if __name__ == "__main__":
    main()
