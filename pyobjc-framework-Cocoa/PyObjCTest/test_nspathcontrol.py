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
        self.failUnlessEqual(m['arguments'][2]['sel_of_type'], 'v@:@')

        self.failUnlessArgIsBOOL(NSPathControl.setDraggingSourceOperationMask_forLocal_, 1)

    @min_os_level('10.5')
    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSPathControlHelper.pathControl_shouldDragPathComponentCell_withPasteboard_)
        self.failUnlessResultHasType(TestNSPathControlHelper.pathControl_validateDrop_, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestNSPathControlHelper.pathControl_acceptDrop_)


if __name__ == "__main__":
    main()
