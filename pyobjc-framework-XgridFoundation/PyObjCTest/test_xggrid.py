from PyObjCTools.TestSupport import TestCase
import XgridFoundation


class TestXGGrid(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(XgridFoundation.XGGrid.isDefault)
