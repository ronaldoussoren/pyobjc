import Foundation  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestNSURLAuthenticationChallenge(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("NSURLAuthenticationChallengeSender")
