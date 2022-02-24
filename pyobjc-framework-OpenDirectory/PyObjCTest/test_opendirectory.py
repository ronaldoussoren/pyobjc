import OpenDirectory
from PyObjCTools.TestSupport import TestCase
import objc


class TestOpenDirectory(TestCase):
    def testConstants(self):
        self.assertIsInstance(OpenDirectory.ODFrameworkErrorDomain, str)

    def testProtocols(self):
        objc.protocolNamed("ODQueryDelegate")

    def testIntegration(self):
        import CFOpenDirectory

        for nm in dir(CFOpenDirectory):
            with self.subTest(nm):
                cfod = getattr(CFOpenDirectory, nm)
                od = getattr(OpenDirectory, nm)

                self.assertIs(cfod, od)
