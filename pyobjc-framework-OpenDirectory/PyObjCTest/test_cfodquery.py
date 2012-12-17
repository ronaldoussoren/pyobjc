from PyObjCTools.TestSupport import *
import CFOpenDirectory

try:
    long
except NameError:
    long = int

class TestCFODNode (TestCase):
    def testMethods(self):
        self.assertIsInstance(CFOpenDirectory.ODQueryGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CFOpenDirectory.ODQueryCreateWithNode)
        self.assertArgIsOut(CFOpenDirectory.ODQueryCreateWithNode, 8)

        self.assertResultIsCFRetained(CFOpenDirectory.ODQueryCreateWithNodeType)
        self.assertArgIsOut(CFOpenDirectory.ODQueryCreateWithNodeType, 8)

        self.assertResultIsCFRetained(CFOpenDirectory.ODQueryCopyResults)
        self.assertArgHasType(CFOpenDirectory.ODQueryCopyResults, 1, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODQueryCopyResults, 2)

        CFOpenDirectory.ODQuerySynchronize

        self.assertArgIsFunction(CFOpenDirectory.ODQuerySetCallback, 1, b"v^{__ODQuery=}@^{__CFError=}^v", True)

        CFOpenDirectory.ODQueryScheduleWithRunLoop
        CFOpenDirectory.ODQueryUnscheduleFromRunLoop

        self.assertArgHasType(CFOpenDirectory.ODQuerySetDispatchQueue, 1, b"^{dispatch_queue_s=}")

if __name__ == "__main__":
    main()
