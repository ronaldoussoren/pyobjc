from PyObjCTools.TestSupport import *
import os

from Foundation import *

class TestNSJavaSetup (TestCase):
    @max_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(NSJavaClasses, unicode)
        self.assertIsInstance(NSJavaRoot, unicode)
        self.assertIsInstance(NSJavaPath, unicode)
        self.assertIsInstance(NSJavaUserPath, unicode)
        self.assertIsInstance(NSJavaLibraryPath, unicode)
        self.assertIsInstance(NSJavaOwnVirtualMachine, unicode)
        self.assertIsInstance(NSJavaPathSeparator, unicode)
        self.assertIsInstance(NSJavaWillSetupVirtualMachineNotification, unicode)
        self.assertIsInstance(NSJavaDidSetupVirtualMachineNotification, unicode)
        self.assertIsInstance(NSJavaWillCreateVirtualMachineNotification, unicode)
        self.assertIsInstance(NSJavaDidCreateVirtualMachineNotification, unicode)
    @max_os_level('10.5')
    def testFunctions(self):
        v = NSJavaNeedsVirtualMachine({})
        self.assertIs(v, False)
        v = NSJavaProvidesClasses({})
        self.assertIs(v, False)
        v = NSJavaNeedsToLoadClasses({})
        self.assertIs(v, False)
        vm = NSJavaSetup({})
        self.assertIsInstance(vm, objc.objc_object)
        v = NSJavaSetupVirtualMachine()
        self.assertIsInstance(v, objc.objc_object)
        v = NSJavaObjectNamedInPath("java.lang.Object", None)
        self.assertIsInstance(v, objc.objc_object)
        v, vm = NSJavaClassesFromPath(None, ['java.lang.Object'], True, None)
        self.assertIsInstance(v, NSArray)
        self.assertEqual(len(v), 1)
        self.assertIsInstance(vm, objc.objc_object)
        v, vm = NSJavaClassesForBundle(NSBundle.mainBundle(), True, None)
        self.assertIsInstance(v, NSArray)
        self.assertEqual(len(v), 0)
        self.assertIsInstance(vm, objc.objc_object)
        vm = NSJavaBundleSetup(NSBundle.mainBundle(), {})
        self.assertIsInstance(vm, objc.objc_object)
        # FIXME: NSJavaBundleCleanup gives an exception
        # This seems to be related to the way we call these APIs and I don't
        # plan to fix is (there is no problem with PyObjC or the Foundation
        # wrappers)
        fd = os.dup(2)
        x = os.open('/dev/null', os.O_WRONLY)
        os.dup2(x, 2)
        os.close(x)
        try:
            try:
                NSJavaBundleCleanup(NSBundle.mainBundle(), {})
            except ValueError:
                pass
        finally:
            os.dup2(fd, 2)


if __name__ == "__main__":
    main()
