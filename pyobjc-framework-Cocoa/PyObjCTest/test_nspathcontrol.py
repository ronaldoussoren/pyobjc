from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPathControlHelper (NSObject):
    def pathControl_shouldDragPathComponentCell_withPasteboard_(self, pc, c, pb): return 1
    def pathControl_validateDrop_(self, pc, dr): return 1
    def pathControl_acceptDrop_(self, pc, dr): return 1


class TestNSPathControl (TestCase):

    @min_os_level("10.5")
    def testMethods(self):
        m = NSPathControl.setDoubleAction_.__metadata__()
        self.assertEqual(m['arguments'][2]['sel_of_type'], b'v@:@')

        self.assertArgIsBOOL(NSPathControl.setDraggingSourceOperationMask_forLocal_, 1)

    @min_os_level('10.5')
    def testProtocols(self):
        self.assertResultIsBOOL(TestNSPathControlHelper.pathControl_shouldDragPathComponentCell_withPasteboard_)
        self.assertResultHasType(TestNSPathControlHelper.pathControl_validateDrop_, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSPathControlHelper.pathControl_acceptDrop_)


if __name__ == "__main__":
    main()
