
from PyObjCTools.TestSupport import *
import CoreServices
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
        self.assertEqual(CoreServices.kLSLaunchDefaults, 0x00000001)
        self.assertEqual(CoreServices.kLSLaunchAndPrint, 0x00000002)
        self.assertEqual(CoreServices.kLSLaunchReserved2, 0x00000004)
        self.assertEqual(CoreServices.kLSLaunchReserved3, 0x00000008)
        self.assertEqual(CoreServices.kLSLaunchReserved4, 0x00000010)
        self.assertEqual(CoreServices.kLSLaunchReserved5, 0x00000020)
        self.assertEqual(CoreServices.kLSLaunchAndDisplayErrors, 0x00000040)
        self.assertEqual(CoreServices.kLSLaunchInhibitBGOnly, 0x00000080)
        self.assertEqual(CoreServices.kLSLaunchDontAddToRecents, 0x00000100)
        self.assertEqual(CoreServices.kLSLaunchDontSwitch, 0x00000200)
        self.assertEqual(CoreServices.kLSLaunchNoParams, 0x00000800)
        self.assertEqual(CoreServices.kLSLaunchAsync, 0x00010000)
        self.assertEqual(CoreServices.kLSLaunchStartClassic, 0x00020000)
        self.assertEqual(CoreServices.kLSLaunchInClassic, 0x00040000)
        self.assertEqual(CoreServices.kLSLaunchNewInstance, 0x00080000)
        self.assertEqual(CoreServices.kLSLaunchAndHide, 0x00100000)
        self.assertEqual(CoreServices.kLSLaunchAndHideOthers, 0x00200000)
        self.assertEqual(CoreServices.kLSLaunchHasUntrustedContents, 0x00400000)

    def testStructs(self):
        v = CoreServices.LSApplicationParameters()
        self.assertHasAttr(v, "version")
        self.assertHasAttr(v, "flags")
        self.assertHasAttr(v, "application")
        self.assertHasAttr(v, "asyncLaunchRefCon")
        self.assertHasAttr(v, "environment")
        self.assertHasAttr(v, "argv")
        self.assertHasAttr(v, "initialEvent")

    def testLSLaunchFSRefSpec(self):
        o = CoreServices.LSLaunchURLSpec()
        self.assertEqual(o.appURL, None)
        self.assertEqual(o.itemURLs, None)
        self.assertEqual(o.passThruParams, None)
        self.assertEqual(o.launchFlags, 0)
        self.assertEqual(o.asyncRefCon, None)

        o = CoreServices.LSLaunchFSRefSpec()
        self.assertEqual(o.appRef, None)
        self.assertEqual(o.numDocs, 0)
        self.assertEqual(o.itemRefs, None)
        self.assertEqual(o.passThruParams, None)
        self.assertEqual(o.launchFlags, 0)
        self.assertEqual(o.asyncRefCon, None)

    def testFunctions(self):
        url = CoreServices.CFURLCreateFromFileSystemRepresentation(None, self.bpath, len(self.bpath), True)

        self.assertArgIsOut(CoreServices.LSOpenCFURLRef, 1)
        ok, u = CoreServices.LSOpenCFURLRef(url, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(u, CoreServices.CFURLRef)

        self.assertArgIsIn(CoreServices.LSOpenItemsWithRole, 0)
        self.assertArgSizeInArg(CoreServices.LSOpenItemsWithRole, 0, 1)
        self.assertArgIsIn(CoreServices.LSOpenItemsWithRole, 3)
        self.assertArgIsIn(CoreServices.LSOpenItemsWithRole, 4)
        self.assertArgIsOut(CoreServices.LSOpenItemsWithRole, 5)
        self.assertArgSizeInArg(CoreServices.LSOpenItemsWithRole, 5, 6)
        ref = objc.FSRef.from_pathname(self.path)
        ok, psns = CoreServices.LSOpenItemsWithRole([ref], 1, CoreServices.kLSRolesAll, None, None, None, 1)
        self.assertIn(ok, (0, -50))
        self.assertIsInstance(psns, (list, tuple))
        for x in psns:
            # Actually a ProcessSerialNumber, but those aren't wrapped yet
            self.assertIsInstance(x, tuple)
            self.assertEquals(len(x), 2)
            self.assertIsInstance(x[0], (int, long))
            self.assertIsInstance(x[1], (int, long))

        self.assertArgIsIn(CoreServices.LSOpenURLsWithRole, 2)
        self.assertArgIsIn(CoreServices.LSOpenURLsWithRole, 3)
        self.assertArgIsOut(CoreServices.LSOpenURLsWithRole, 4)
        self.assertArgSizeInArg(CoreServices.LSOpenURLsWithRole, 4, 5)
        ok, psns = CoreServices.LSOpenURLsWithRole([url], CoreServices.kLSRolesAll, None, None, None, 1)
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
        self.assertArgIsIn(CoreServices.LSOpenApplication, 0)
        self.assertArgIsOut(CoreServices.LSOpenApplication, 1)
        params = CoreServices.LSApplicationParameters(
                version=0,
                flags = CoreServices.kLSLaunchDefaults,
                application = objc.FSRef.from_pathname('/Applications/Utilities/Terminal.app'),
                asyncLaunchRefCon = None,
                environment = None,
                argv = [b"Terminal".decode('latin1')],
                initialEvent = None,
            )

        # Call will fail for now, 'application' is an FSRef pointers and
        # pyobjc-core isn't smart enough to deal with that.
        ok, psn = CoreServices.LSOpenApplication(params, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(psn, (int, long))


    def testFSRef(self):
        # Functions using structs we don't support, probably need
        # manual wrappers
        self.assertArgIsIn(CoreServices.LSOpenFromRefSpec, 0)
        self.assertArgIsOut(CoreServices.LSOpenFromRefSpec, 1)
        self.assertArgIsIn(CoreServices.LSOpenFromURLSpec, 0)
        self.assertArgIsOut(CoreServices.LSOpenFromURLSpec, 1)

if __name__ == "__main__":
    main()
