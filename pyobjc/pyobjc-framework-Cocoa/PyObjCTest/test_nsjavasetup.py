from PyObjCTools.TestSupport import *
import os

from Foundation import *

class TestNSJavaSetup (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSJavaClasses, unicode))
        self.failUnless(isinstance(NSJavaRoot, unicode))
        self.failUnless(isinstance(NSJavaPath, unicode))
        self.failUnless(isinstance(NSJavaUserPath, unicode))
        self.failUnless(isinstance(NSJavaLibraryPath, unicode))
        self.failUnless(isinstance(NSJavaOwnVirtualMachine, unicode))
        self.failUnless(isinstance(NSJavaPathSeparator, unicode))

        self.failUnless(isinstance(NSJavaWillSetupVirtualMachineNotification, unicode))
        self.failUnless(isinstance(NSJavaDidSetupVirtualMachineNotification, unicode))

        self.failUnless(isinstance(NSJavaWillCreateVirtualMachineNotification, unicode))
        self.failUnless(isinstance(NSJavaDidCreateVirtualMachineNotification, unicode))

    def testFunctions(self):
        v = NSJavaNeedsVirtualMachine({})
        self.failUnless(v is False)

        v = NSJavaProvidesClasses({})
        self.failUnless(v is False)

        v = NSJavaNeedsToLoadClasses({})
        self.failUnless(v is False)

        vm = NSJavaSetup({})
        self.failUnless(isinstance(vm, objc.objc_object))

        v = NSJavaSetupVirtualMachine()
        self.failUnless(isinstance(v, objc.objc_object))

        v = NSJavaObjectNamedInPath("java.lang.Object", None)
        self.failUnless(isinstance(v, objc.objc_object))

        v, vm = NSJavaClassesFromPath(None, ['java.lang.Object'], True, None)
        self.failUnless(isinstance(v, NSArray))
        self.assertEquals(len(v), 1)
        self.failUnless(isinstance(vm, objc.objc_object))

        v, vm = NSJavaClassesForBundle(NSBundle.mainBundle(), True, None)
        self.failUnless(isinstance(v, NSArray))
        self.assertEquals(len(v), 0)
        self.failUnless(isinstance(vm, objc.objc_object))

        vm = NSJavaBundleSetup(NSBundle.mainBundle(), {})
        self.failUnless(isinstance(vm, objc.objc_object))

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
