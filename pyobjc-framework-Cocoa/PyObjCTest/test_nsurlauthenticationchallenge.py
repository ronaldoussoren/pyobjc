import Foundation  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestNSURLAuthenticationChallenge(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("NSURLAuthenticationChallengeSender", Foundation)
