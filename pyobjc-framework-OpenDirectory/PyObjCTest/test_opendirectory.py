import OpenDirectory
from PyObjCTools.TestSupport import TestCase


class TestOpenDirectory(TestCase):
    def testConstants(self):
        self.assertIsInstance(OpenDirectory.ODFrameworkErrorDomain, str)

    def testProtocols(self):
        self.assertProtocolExists("ODQueryDelegate")

    def testIntegration(self):
        import CFOpenDirectory

        for nm in dir(CFOpenDirectory):
            with self.subTest(nm):
                cfod = getattr(CFOpenDirectory, nm)
                od = getattr(OpenDirectory, nm)

                self.assertIs(cfod, od, f"{nm!r}, {type(cfod)}, {type(od)}")


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(OpenDirectory)
