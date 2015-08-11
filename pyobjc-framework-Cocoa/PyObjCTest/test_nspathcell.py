from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPathCell (TestCase):
    def testConstants(self):
        self.assertEqual(NSPathStyleStandard, 0)
        self.assertEqual(NSPathStyleNavigationBar, 1)
        self.assertEqual(NSPathStylePopUp, 2)

    def testMethods(self):
        m = NSPathCell.setDoubleAction_.__metadata__()
        self.assertEqual(m['arguments'][2]['sel_of_type'], b'v@:@')

    @min_sdk_level('10.10')
    def testProtocols(self):
        objc.protocolNamed('NSPathCellDelegate')

if __name__ == "__main__":
    main()
