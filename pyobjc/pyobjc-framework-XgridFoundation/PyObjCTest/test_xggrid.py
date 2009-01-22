
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGGrid (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(XGGrid.isDefault)


if __name__ == "__main__":
    main()
