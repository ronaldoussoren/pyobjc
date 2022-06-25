from PyObjCTools.TestSupport import TestCase, min_sdk_level
import PhotosUI  # noqa: F401


class TestPHProjectTypeDescriptionDataSource(TestCase):
    @min_sdk_level("10.14")
    def testProtocols(self):
        self.assertProtocolExists("PHProjectTypeDescriptionDataSource")
        self.assertProtocolExists("PHProjectTypeDescriptionInvalidator")
