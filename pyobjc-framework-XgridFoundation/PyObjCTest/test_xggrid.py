
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGGrid (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(XGGrid.isDefault)


if __name__ == "__main__":
    main()
