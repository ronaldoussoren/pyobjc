import os
import objc

import Foundation
from PyObjCTools.TestSupport import TestCase, max_os_level


class TestNSJavaSetup(TestCase):
    @max_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Foundation.NSJavaClasses, str)
        self.assertIsInstance(Foundation.NSJavaRoot, str)
        self.assertIsInstance(Foundation.NSJavaPath, str)
        self.assertIsInstance(Foundation.NSJavaUserPath, str)
        self.assertIsInstance(Foundation.NSJavaLibraryPath, str)
        self.assertIsInstance(Foundation.NSJavaOwnVirtualMachine, str)
        self.assertIsInstance(Foundation.NSJavaPathSeparator, str)
        self.assertIsInstance(Foundation.NSJavaWillSetupVirtualMachineNotification, str)
        self.assertIsInstance(Foundation.NSJavaDidSetupVirtualMachineNotification, str)
        self.assertIsInstance(
            Foundation.NSJavaWillCreateVirtualMachineNotification, str
        )
        self.assertIsInstance(Foundation.NSJavaDidCreateVirtualMachineNotification, str)

    @max_os_level("10.5")
    def testFunctions(self):
        v = Foundation.NSJavaNeedsVirtualMachine({})
        self.assertIs(v, False)
        v = Foundation.NSJavaProvidesClasses({})
        self.assertIs(v, False)
        v = Foundation.NSJavaNeedsToLoadClasses({})
        self.assertIs(v, False)
        vm = Foundation.NSJavaSetup({})
        self.assertIsInstance(vm, objc.objc_object)
        v = Foundation.NSJavaSetupVirtualMachine()
        self.assertIsInstance(v, objc.objc_object)
        v = Foundation.NSJavaObjectNamedInPath("java.lang.Object", None)
        self.assertIsInstance(v, objc.objc_object)
        v, vm = Foundation.NSJavaClassesFromPath(None, ["java.lang.Object"], True, None)
        self.assertIsInstance(v, Foundation.NSArray)
        self.assertEqual(len(v), 1)
        self.assertIsInstance(vm, objc.objc_object)
        v, vm = Foundation.NSJavaClassesForBundle(
            Foundation.NSBundle.mainBundle(), True, None
        )
        self.assertIsInstance(v, Foundation.NSArray)
        self.assertEqual(len(v), 0)
        self.assertIsInstance(vm, objc.objc_object)
        vm = Foundation.NSJavaBundleSetup(Foundation.NSBundle.mainBundle(), {})
        self.assertIsInstance(vm, objc.objc_object)
        # FIXME: Foundation.NSJavaBundleCleanup gives an exception
        # This seems to be related to the way we call these APIs and I don't
        # plan to fix is (there is no problem with PyObjC or the Foundation
        # wrappers)
        fd = os.dup(2)
        x = os.open("/dev/null", os.O_WRONLY)
        os.dup2(x, 2)
        os.close(x)
        try:
            try:
                Foundation.NSJavaBundleCleanup(Foundation.NSBundle.mainBundle(), {})
            except ValueError:
                pass
        finally:
            os.dup2(fd, 2)
