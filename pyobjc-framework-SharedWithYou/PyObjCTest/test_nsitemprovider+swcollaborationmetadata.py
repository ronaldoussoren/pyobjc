from PyObjCTools.TestSupport import TestCase, min_os_level

import SharedWithYou


class TestNSItemProvider_SWCollaborationMetadata(TestCase):
    def test_constants(self):
        self.assertIsInstance(SharedWithYou.SWCollaborationMetadataTypeIdentifier, str)

    @min_os_level("27.0")
    def test_constants27_0(self):
        self.assertIsInstance(SharedWithYou.SWCopyRepresentationTypeIdentifier, str)
