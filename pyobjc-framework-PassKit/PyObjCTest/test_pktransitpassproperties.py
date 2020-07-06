from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKTransitPassProperties(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(PassKit.PKTransitPassProperties.isInStation)
        self.assertResultIsBOOL(PassKit.PKTransitPassProperties.isBlacklisted)
