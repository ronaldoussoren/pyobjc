
from PyObjCTools.TestSupport import *
import LaunchServices
import sys
import os

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
        self.assertEqual(LaunchServices.kLSLaunchDefaults, 0x00000001)
        self.assertEqual(LaunchServices.kLSLaunchAndPrint, 0x00000002)
        self.assertEqual(LaunchServices.kLSLaunchReserved2, 0x00000004)
        self.assertEqual(LaunchServices.kLSLaunchReserved3, 0x00000008)
        self.assertEqual(LaunchServices.kLSLaunchReserved4, 0x00000010)
        self.assertEqual(LaunchServices.kLSLaunchReserved5, 0x00000020)
        self.assertEqual(LaunchServices.kLSLaunchAndDisplayErrors, 0x00000040)
        self.assertEqual(LaunchServices.kLSLaunchInhibitBGOnly, 0x00000080)
        self.assertEqual(LaunchServices.kLSLaunchDontAddToRecents, 0x00000100)
        self.assertEqual(LaunchServices.kLSLaunchDontSwitch, 0x00000200)
        self.assertEqual(LaunchServices.kLSLaunchNoParams, 0x00000800)
        self.assertEqual(LaunchServices.kLSLaunchAsync, 0x00010000)
        self.assertEqual(LaunchServices.kLSLaunchStartClassic, 0x00020000)
        self.assertEqual(LaunchServices.kLSLaunchInClassic, 0x00040000)
        self.assertEqual(LaunchServices.kLSLaunchNewInstance, 0x00080000)
        self.assertEqual(LaunchServices.kLSLaunchAndHide, 0x00100000)
        self.assertEqual(LaunchServices.kLSLaunchAndHideOthers, 0x00200000)
        self.assertEqual(LaunchServices.kLSLaunchHasUntrustedContents, 0x00400000)

    def testStructs(self):
        v = LaunchServices.LSApplicationParameters()
        self.assertHasAttr(v, "version")
        self.assertHasAttr(v, "flags")
        self.assertHasAttr(v, "application")
        self.assertHasAttr(v, "asyncLaunchRefCon")
        self.assertHasAttr(v, "environment")
        self.assertHasAttr(v, "argv")
        self.assertHasAttr(v, "initialEvent")

    def testLSLaunchFSRefSpec(self):
        o = LaunchServices.LSLaunchURLSpec()
        self.assertEqual(o.appURL, None)
        self.assertEqual(o.itemURLs, None)
        self.assertEqual(o.passThruParams, None)
        self.assertEqual(o.launchFlags, 0)
        self.assertEqual(o.asyncRefCon, None)

        o = LaunchServices.LSLaunchFSRefSpec()
        self.assertEqual(o.appRef, None)
        self.assertEqual(o.numDocs, 0)
        self.assertEqual(o.itemRefs, None)
        self.assertEqual(o.passThruParams, None)
        self.assertEqual(o.launchFlags, 0)
        self.assertEqual(o.asyncRefCon, None)

    def testFunctions(self):
        url = LaunchServices.CFURLCreateFromFileSystemRepresentation(None, self.bpath, len(self.bpath), True)

        self.assertArgIsOut(LaunchServices.LSOpenCFURLRef, 1)
        ok, u = LaunchServices.LSOpenCFURLRef(url, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(u, LaunchServices.CFURLRef)

        self.assertArgIsIn(LaunchServices.LSOpenItemsWithRole, 0)
        self.assertArgSizeInArg(LaunchServices.LSOpenItemsWithRole, 0, 1)
        self.assertArgIsIn(LaunchServices.LSOpenItemsWithRole, 3)
        self.assertArgIsIn(LaunchServices.LSOpenItemsWithRole, 4)
        self.assertArgIsOut(LaunchServices.LSOpenItemsWithRole, 5)
        self.assertArgSizeInArg(LaunchServices.LSOpenItemsWithRole, 5, 6)
        ref = objc.FSRef.from_pathname(self.path)
        ok, psns = LaunchServices.LSOpenItemsWithRole([ref], 1, LaunchServices.kLSRolesAll, None, None, None, 1)
        self.assertIn(ok, (0, -50))
        self.assertIsInstance(psns, (list, tuple))
        for x in psns:
            # Actually a ProcessSerialNumber, but those aren't wrapped yet
            self.assertIsInstance(x, tuple)
            self.assertEquals(len(x), 2)
            self.assertIsInstance(x[0], (int, long))
            self.assertIsInstance(x[1], (int, long))

        self.assertArgIsIn(LaunchServices.LSOpenURLsWithRole, 2)
        self.assertArgIsIn(LaunchServices.LSOpenURLsWithRole, 3)
        self.assertArgIsOut(LaunchServices.LSOpenURLsWithRole, 4)
        self.assertArgSizeInArg(LaunchServices.LSOpenURLsWithRole, 4, 5)
        ok, psns = LaunchServices.LSOpenURLsWithRole([url], LaunchServices.kLSRolesAll, None, None, None, 1)
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
        self.assertArgIsIn(LaunchServices.LSOpenApplication, 0)
        self.assertArgIsOut(LaunchServices.LSOpenApplication, 1)
        params = LaunchServices.LSApplicationParameters(
                version=0,
                flags = LaunchServices.kLSLaunchDefaults,
                application = objc.FSRef.from_pathname('/Applications/Utilities/Terminal.app'),
                asyncLaunchRefCon = None,
                environment = None,
                argv = [b"Terminal".decode('latin1')],
                initialEvent = None,
            )

        # Call will fail for now, 'application' is an FSRef pointers and
        # pyobjc-core isn't smart enough to deal with that.
        ok, psn = LaunchServices.LSOpenApplication(params, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(psn, (int, long))


    def testFSRef(self):
        # Functions using structs we don't support, probably need
        # manual wrappers
        self.assertArgIsIn(LaunchServices.LSOpenFromRefSpec, 0)
        self.assertArgIsOut(LaunchServices.LSOpenFromRefSpec, 1)
        self.assertArgIsIn(LaunchServices.LSOpenFromURLSpec, 0)
        self.assertArgIsOut(LaunchServices.LSOpenFromURLSpec, 1)

if __name__ == "__main__":
    main()
