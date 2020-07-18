from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKSuicaPassProperties(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(PassKit.PKSuicaPassProperties.isInStation)
        self.assertResultIsBOOL(PassKit.PKSuicaPassProperties.isInShinkansenStation)
        self.assertResultIsBOOL(
            PassKit.PKSuicaPassProperties.isBalanceAllowedForCommute
        )
        self.assertResultIsBOOL(
            PassKit.PKSuicaPassProperties.isLowBalanceGateNotificationEnabled
        )
        self.assertResultIsBOOL(PassKit.PKSuicaPassProperties.isGreenCarTicketUsed)
        self.assertResultIsBOOL(PassKit.PKSuicaPassProperties.isBlacklisted)
