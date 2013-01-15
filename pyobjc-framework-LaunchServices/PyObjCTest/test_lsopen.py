
from PyObjCTools.TestSupport import *
from LaunchServices import *
import sys
import os

try:
    long
except NameError:
    long = int

class TestLSOpen (TestCase):
    def setUp(self):
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dummy.txt')
        fp = open(self.path, 'w')
        fp.write('test contents')
        fp.close()

        self.bpath = self.path.encode('utf-8')

    def tearDown(self):
        if os.path.exists(self.path):
            os.unlink(self.path)

    def testConstants(self):
        self.assertEqual(kLSLaunchDefaults, 0x00000001)
        self.assertEqual(kLSLaunchAndPrint, 0x00000002)
        self.assertEqual(kLSLaunchReserved2, 0x00000004)
        self.assertEqual(kLSLaunchReserved3, 0x00000008)
        self.assertEqual(kLSLaunchReserved4, 0x00000010)
        self.assertEqual(kLSLaunchReserved5, 0x00000020)
        self.assertEqual(kLSLaunchAndDisplayErrors, 0x00000040)
        self.assertEqual(kLSLaunchInhibitBGOnly, 0x00000080)
        self.assertEqual(kLSLaunchDontAddToRecents, 0x00000100)
        self.assertEqual(kLSLaunchDontSwitch, 0x00000200)
        self.assertEqual(kLSLaunchNoParams, 0x00000800)
        self.assertEqual(kLSLaunchAsync, 0x00010000)
        self.assertEqual(kLSLaunchStartClassic, 0x00020000)
        self.assertEqual(kLSLaunchInClassic, 0x00040000)
        self.assertEqual(kLSLaunchNewInstance, 0x00080000)
        self.assertEqual(kLSLaunchAndHide, 0x00100000)
        self.assertEqual(kLSLaunchAndHideOthers, 0x00200000)
        self.assertEqual(kLSLaunchHasUntrustedContents, 0x00400000)

    def testStructs(self):
        v = LSApplicationParameters()
        self.assertHasAttr(v, "version")
        self.assertHasAttr(v, "flags")
        self.assertHasAttr(v, "application")
        self.assertHasAttr(v, "asyncLaunchRefCon")
        self.assertHasAttr(v, "environment")
        self.assertHasAttr(v, "argv")
        self.assertHasAttr(v, "initialEvent")

    def testLSLaunchFSRefSpec(self):
        o = LSLaunchURLSpec()
        self.assertEqual(o.appURL, None)
        self.assertEqual(o.itemURLs, None)
        self.assertEqual(o.passThruParams, None)
        self.assertEqual(o.launchFlags, 0)
        self.assertEqual(o.asyncRefCon, None)

        o = LSLaunchFSRefSpec()
        self.assertEqual(o.appRef, None)
        self.assertEqual(o.numDocs, 0)
        self.assertEqual(o.itemRefs, None)
        self.assertEqual(o.passThruParams, None)
        self.assertEqual(o.launchFlags, 0)
        self.assertEqual(o.asyncRefCon, None)

    @expectedFailure
    def testUnsupportedStructs(self):
        self.fail("LSLaunchFSRefSpec")


    def testFunctions(self):
        url = CFURLCreateFromFileSystemRepresentation(None, self.bpath, len(self.bpath), True)

        self.assertArgIsOut(LSOpenCFURLRef, 1)
        ok, u = LSOpenCFURLRef(url, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(u, CFURLRef)

        self.assertArgIsIn(LSOpenItemsWithRole, 0)
        self.assertArgSizeInArg(LSOpenItemsWithRole, 0, 1)
        self.assertArgIsIn(LSOpenItemsWithRole, 3)
        self.assertArgIsIn(LSOpenItemsWithRole, 4)
        self.assertArgIsOut(LSOpenItemsWithRole, 5)
        self.assertArgSizeInArg(LSOpenItemsWithRole, 5, 6)
        ref = objc.FSRef.from_pathname(self.path)
        ok, psns = LSOpenItemsWithRole([ref], 1, kLSRolesAll, None, None, None, 1)
        self.assertEquals(ok, 0)
        self.assertIsInstance(psns, (list, tuple))
        for x in psns:
            # Actually a ProcessSerialNumber, but those aren't wrapped yet
            self.assertIsInstance(x, tuple)
            self.assertEquals(len(x), 2)
            self.assertIsInstance(x[0], (int, long))
            self.assertIsInstance(x[1], (int, long))

        self.assertArgIsIn(LSOpenURLsWithRole, 2)
        self.assertArgIsIn(LSOpenURLsWithRole, 3)
        self.assertArgIsOut(LSOpenURLsWithRole, 4)
        self.assertArgSizeInArg(LSOpenURLsWithRole, 4, 5)
        ok, psns = LSOpenURLsWithRole([url], kLSRolesAll, None, None, None, 1)
        self.assertEquals(ok, 0)
        self.assertIsInstance(psns, (list, tuple))
        for x in psns:
            # Actually a ProcessSerialNumber, but those aren't wrapped yet
            self.assertIsInstance(x, tuple)
            self.assertEquals(len(x), 2)
            self.assertIsInstance(x[0], (int, long))
            self.assertIsInstance(x[1], (int, long))



    @expectedFailure
    def testUnsupportedFunctions(self):
        self.assertArgIsIn(LSOpenApplication, 0)
        self.assertArgIsOut(LSOpenApplication, 1)
        params = LSApplicationParameters(
                version=0,
                flags = kLSLaunchDefaults,
                application = objc.FSRef.from_pathname('/Applications/Utilities/Terminal.app'),
                asyncLaunchRefCon = None,
                environment = None,
                argv = [b"Terminal".decode('latin1')],
                initialEvent = None,
            )

        # Call will fail for now, 'application' is an FSRef pointers and
        # pyobjc-core isn't smart enough to deal with that.
        ok, psn = LSOpenApplication(params, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(psn, (int, long))


    @expectedFailure
    def testFSRef(self):
        # Functions using structs we don't support, probably need
        # manual wrappers
        self.fail("LSOpenFromRefSpec")
        self.fail("LSOpenFromURLSpec")

if __name__ == "__main__":
    main()
