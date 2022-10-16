from PyObjCTools.TestSupport import TestCase

import ThreadNetwork


class THClient(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(ThreadNetwork.THClient.retrieveAllCredentials_, 0, b"v@@")
        self.assertArgIsBlock(
            ThreadNetwork.THClient.deleteCredentialsForBorderAgent_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            ThreadNetwork.THClient.retrieveCredentialsForBorderAgent_completion_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            ThreadNetwork.THClient.storeCredentialsForBorderAgent_activeOperationalDataSet_completion_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            ThreadNetwork.THClient.retrievePreferredCredentials_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            ThreadNetwork.THClient.retrieveCredentialsForExtendedPANID_completion_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            ThreadNetwork.THClient.checkPreferredNetworkForActiveOperationalDataset_completion_,
            1,
            b"vZ",
        )
