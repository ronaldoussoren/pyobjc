from PyObjCTools.TestSupport import TestCase
import objc
import PassKit


class TestPKAddTicketConfiguration(TestCase):
    def test_constants(self):
        self.assertEqual(PassKit.PKAddTicketConfigurationPrimaryActionAdd, 0)
        self.assertEqual(PassKit.PKAddTicketConfigurationPrimaryActionShare, 1)

    def test_methods(self):
        self.assertArgIsBlock(
            PassKit.PKAddTicketConfiguration.preflightWithCompletion_,
            0,
            b"v" + objc._C_NSBOOL,
        )
