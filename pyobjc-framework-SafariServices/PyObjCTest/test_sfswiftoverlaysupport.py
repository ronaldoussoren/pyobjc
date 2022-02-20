from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFContentBlockerManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SafariServices.SFSafariServicesVersion)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(SafariServices.SFSafariServicesVersion10_0, 0)
        self.assertEqual(SafariServices.SFSafariServicesVersion10_1, 1)
        self.assertEqual(SafariServices.SFSafariServicesVersion11_0, 2)
        self.assertEqual(SafariServices.SFSafariServicesVersion12_0, 3)
        self.assertEqual(SafariServices.SFSafariServicesVersion12_1, 4)
        self.assertEqual(SafariServices.SFSafariServicesVersion13_0, 5)
