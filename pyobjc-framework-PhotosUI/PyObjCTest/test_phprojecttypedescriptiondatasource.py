from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc
import PhotosUI  # noqa: F401


class TestPHProjectTypeDescriptionDataSource(TestCase):
    @min_sdk_level("10.14")
    def testProtocols(self):
        objc.protocolNamed("PHProjectTypeDescriptionDataSource")
        objc.protocolNamed("PHProjectTypeDescriptionInvalidator")
