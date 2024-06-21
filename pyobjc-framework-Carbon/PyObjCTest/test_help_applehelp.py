from PyObjCTools.TestSupport import TestCase

import Carbon


class TestHelp_AppleHelp(TestCase):
    def test_enum(self):
        self.assertEqual(Carbon.kAHInternalErr, -10790)
        self.assertEqual(Carbon.kAHInternetConfigPrefErr, -10791)

        self.assertEqual(Carbon.kAHTOCTypeUser, 0)
        self.assertEqual(Carbon.kAHTOCTypeDeveloper, 1)

    def test_functions(self):
        Carbon.AHSearch
        Carbon.AHGotoMainTOC
        Carbon.AHGotoPage
        Carbon.AHLookupAnchor
        self.assertArgIsIn(Carbon.AHRegisterHelpBook, 0)
        Carbon.AHRegisterHelpBookWithURL
