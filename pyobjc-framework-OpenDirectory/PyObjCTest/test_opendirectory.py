from PyObjCTools.TestSupport import *
import objc
import OpenDirectory

class TestOpenDirectory (TestCase):
    def testConstants(self):
        self.assertIsInstance(OpenDirectory.ODFrameworkErrorDomain, unicode)

    def testProtocols(self):
        objc.protocolNamed('ODQueryDelegate')

    def testIntegration(self):
        import CFOpenDirectory

        for nm in dir(CFOpenDirectory):
            cfod = getattr(CFOpenDirectory, nm)
            od = getattr(OpenDirectory, nm)

            assert cfod is od


if __name__ == "__main__":
    main()
