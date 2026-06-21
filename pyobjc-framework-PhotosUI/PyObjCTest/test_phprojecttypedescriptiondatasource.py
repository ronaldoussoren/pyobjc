from PyObjCTools.TestSupport import TestCase, min_sdk_level
import PhotosUI  # noqa: F401


class TestPHProjectTypeDescriptionDataSource(TestCase):
    @min_sdk_level("10.14")
    def test_protocols(self):
        self.assertProtocolExists("PHProjectTypeDescriptionDataSource", PhotosUI)
        self.assertProtocolExists("PHProjectTypeDescriptionInvalidator", PhotosUI)
